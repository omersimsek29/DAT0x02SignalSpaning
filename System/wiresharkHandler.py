import numpy as np
import pandas as pd
import math
import threading
import os
import random
import string
import time
from os.path import expanduser
import socket
import pickle

### TSHARK KOMMANDON

#tshark -D för att se en lista av alla tillgängliga interfaces.

#kommando för att capturea och spara till test1.pcap, capture kommer att avbrytas när 1000 packet har captureats
# alternativt när en sekund gått.
#tshark -i 1 -w test1.pcap -a duration:1  -a packets:1000

### GLOBALS
randomFilenameLength = 10
pcapFileNames = []
csvFileNames = []
end = False
host = '192.168.1.105' #Hårdkodad ip-adress till server som måste anges
port = 5001
startStr = 'start'
quitStr = 'quit'
semaphore = threading.Semaphore(0)

### SETTINGS
pd.set_option("display.max_rows", None, "display.max_columns", None) # detta gör att man kan printa dataframes snyggt
home = expanduser("~")
os.chdir(home) # valt en dierctory för alla filer som är lätt att se. 
mySocket = socket.socket()
mySocket.connect((host,port))

### FUNKTIONER

#capturear och sparar med slumpmässigt namn som pcap
def captureAndSave(duration, packets, interfaceIndex):
    home = expanduser("~") # kan förmodligen tas bort utan problem, men har inte möjlighet att testa så vågar inte ändra. 
    os.chdir(home) # kan förmodligen tas bort utan problem, men har inte möjlighet att testa så vågar inte ändra. 
    filename = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(randomFilenameLength))
    # säkerställ att airmon körs, om 0 packet captureas är det troligen pga det
    os.system('tshark -i' + str(interfaceIndex) + ' -w ' + filename + '.pcap -a duration:' + str(duration) + ' -a packets:' + str(packets)) # kör wireshark capture en viss duration eller antal packet, beroende på vad som sker först. 
    pcapFileNames.append(filename) # sparar filnamnen som använts för pcap
    semaphore.release() # semaforen signalerar att pcap filen är klar och att den går att göra om till csv fil.
    if end == False: # om end == True --> avsluta program
        captureAndSave(duration, packets, interfaceIndex)
    else:     
        removeFile(home + '/' + filename + '.pcap')

#skapar en csv med samma namn som pcap filen med vissa intressanta fält enbart.
def createCSVFromCapture(): 
    home = expanduser("~") # kan förmodligen tas bort utan problem, men har inte möjlighet att testa så vågar inte ändra. 
    os.chdir(home) # kan förmodligen tas bort utan problem, men har inte möjlighet att testa så vågar inte ändra. 
    semaphore.acquire() # då pcap filen är färdig fortsätter koden
    while(len(pcapFileNames) == 0): # gör detta pga jag är osäker på om ett race condition kan uppstå eller ej, lade till detta för att undvika det
        time.sleep(0.1)
    captureFile = pcapFileNames[0]
    os.system('tshark -r ' + captureFile + '.pcap -o\'column.format:"Dport","%D","Protocol","%p"\' -T fields -E separator=, -E header=y -e wlan.da -e wlan.sa -e wlan.ssid -e wlan_radio.signal_dbm -e wlan.ra -e wlan.ta > ' + captureFile + '.csv') # går pcap till csv fil med intressanta fält för oss
    csvFileNames.append(captureFile) # använder samma namn som pcap fast .csv
    pcapFileNames.pop(0)
    if end == False:
        extractFromCsv('emils privata') # skickar data till server och tar bort angivet ssid
        createCSVFromCapture() # upprepar processen att skapa csv filer från pcap
    else: # om end = True kommer filerna inte tas bort, och filerna kan inte alltid tas bort så här tidigt
        removeFile(home + '/' + captureFile + '.pcap')
        removeFile(home + '/' + captureFile + '.csv')

# tar bort en fil med given path
def removeFile(path):
    if os.path.exists(path):
        os.remove(path)

#plockar ut nyckeldata från csvn och beräknar medelvärdet för signalstrykan om en transmitter har flera packet i samma caoture.
def extractFromCsv(ssid = ''):
    while(len(csvFileNames) == 0):
        time.sleep(0.1)
    # går om csv till dataframe
    wireshark_data = pd.read_csv(home + '/' + csvFileNames[0] + '.csv') # kanske ska lägga till errorbadllines = False
    #filterSource("c0:ee:fb:89:a6:cf", wireshark_data)
    filename = csvFileNames.pop(0)
    # tar bort filerna som skapats
    removeFile(home + '/' + filename + '.csv') 
    removeFile(home + '/' + filename + '.pcap')
    extracted_data = pd.DataFrame(columns=['source', 'signal strength', 'packets'])
    if ssid != '' :
        wireshark_data = filterSSID(ssid, wireshark_data)
    for index, row in wireshark_data.iterrows():
        if (not pd.isna(wireshark_data.iloc[index]['wlan.ta'])) and (not (wireshark_data.iloc[index]['wlan.ta'] in extracted_data['source'].values)):
            nf = wireshark_data.loc[wireshark_data['wlan.ta'] == wireshark_data.iloc[index]['wlan.ta']]
            extracted_data = extracted_data.append({'source': wireshark_data.iloc[index]['wlan.ta'], 'signal strength': nf['wlan_radio.signal_dbm'].mean(), 'packets' : len(nf)}, ignore_index=True) # gör i ordning den extraherade data och beräknar medelvärde för signalstyrka
    print('Done with extracting data')
    print(extracted_data)
    data = pickle.dumps(extracted_data) # serializerar data
    sendData(data) # skickar data

#Filtrerar bort angivet ssid från dataframe(obs måste innehålla wlan.ssid fältet som fås från ursprungs csvn)
def filterSSID(ssid, data): # data kommer att droppa alla rader som innehåller angivet ssid
    indexes = data[data['wlan.ssid'] == ssid].index
    data.drop(indexes, inplace=True)
    return data

# Filtrerar bort alla sources förutom angiven source (för att underlätta testning av lokalisering)
def filterSource(source, data):
    data = data[data['source'] == source] # inte säker på om jag dessutom behöver returnera data eller om det uppdateras automatiskt 

#skickar data till server
def sendData(message): 
    mySocket.sendall(message)

#skickar disconnect till servern och stänger ner våran socket.
def disconnect():
    mySocket.send(str.encode('disconnect'))
    mySocket.close()
    global end
    end = True

# Väntar på att servern ska signalera start
def waitForStart(socket):
    data = socket.recv(1024).decode()
    if data == startStr:
        startAllThreads()
    else:
        print('error, implementera')

# Skapar trådkopplingen samt pipelinen för data capture, extraction och överföring till server
def startAllThreads():
    capture_thread = threading.Thread(target=captureAndSave, args=[1, 500, 1])
    extraction_thread = threading.Thread(target=createCSVFromCapture)
    capture_thread.start()
    extraction_thread.start()
    
# ankarloop som pågår tills programmet avslutas 
def consoleLoop():
    while True:
        input_line = input()
        if input_line == quitStr:
            disconnect()

### TRÅDAR
start_thread = threading.Thread(target = waitForStart, args = [mySocket])
start_thread.start()

consoleLoop() # kör captures tills keyboardinteruppt eller användare avslutar server eller ankare
#time.sleep(60)

disconnect()
### EGNA TANKAR 

# om transformeringen av data tar längre tid än caputring av packet kommer bottleneck problem att uppstå
# de tillfälliga filerna som skapas får jag inte glömma att ta bort efter(sparar atm för att se resultaten lättare)




