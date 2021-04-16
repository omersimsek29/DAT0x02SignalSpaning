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
host = '192.168.0.100' #Detta är min hem ip-adress, dock tror jag det är den lokala ip-adressen eftersom what'smyipadress.com ger mig en annan
port = 5000
startStr = 'start'
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
    home = expanduser("~") # gör detta igen för att vara övertydlig, räcker att köra en gång globalt egentligen
    os.chdir(home)
    filename = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(randomFilenameLength))
    # säkerställ att airmon körs, om 0 packet captureas är det troligen pga det
    os.system('tshark -i' + str(interfaceIndex) + ' -w ' + filename + '.pcap -a duration:' + str(duration) + ' -a packets:' + str(packets))
    pcapFileNames.append(filename)
    semaphore.release()
    if end == False:
        captureAndSave(duration, packets, interfaceIndex)

#skapar en csv med samma namn som pcap filen med vissa intressanta fält enbart.
def createCSVFromCapture(): 
    home = expanduser("~")
    os.chdir(home)
    semaphore.acquire()
    while(len(pcapFileNames) == 0): # gör detta pga jag är osäker på om ett race condition kan uppstå eller ej, lade till detta för att undvika det
        time.sleep(0.1)
    captureFile = pcapFileNames[0]
    os.system('tshark -r ' + captureFile + '.pcap -o\'column.format:"Dport","%D","Protocol","%p"\' -T fields -E separator=, -E header=y -e wlan.da -e wlan.sa -e wlan.ssid -e wlan_radio.signal_dbm -e wlan.ra -e wlan.ta > ' + captureFile + '.csv')
    csvFileNames.append(captureFile)
    pcapFileNames.pop(0)
    if end == False:
        extractFromCsv()
        createCSVFromCapture()

#plockar ut nyckeldata från csvn och beräknar medelvärdet för signalstrykan om en transmitter har flera packet i samma caoture.
def extractFromCsv(ssid = ''):
    while(len(csvFileNames) == 0):
        time.sleep(0.1)
    wireshark_data = pd.read_csv(home + '/' + csvFileNames[0] + '.csv')
    csvFileNames.pop(0)
    extracted_data = pd.DataFrame(columns=['source', 'signal strength', 'packets'])
    if ssid != '' :
        wireshark_data = filterSSID(ssid, wireshark_data)
    for index, row in wireshark_data.iterrows():
        if (not pd.isna(wireshark_data.iloc[index]['wlan.ta'])) and (not (wireshark_data.iloc[index]['wlan.ta'] in extracted_data['source'].values)):
            nf = wireshark_data.loc[wireshark_data['wlan.ta'] == wireshark_data.iloc[index]['wlan.ta']]
            extracted_data = extracted_data.append({'source': wireshark_data.iloc[index]['wlan.ta'], 'signal strength': nf['wlan_radio.signal_dbm'].mean(), 'packets' : len(nf)}, ignore_index=True)
    print('Done with extracting data')
    print(extracted_data)
    data = pickle.dumps(extracted_data)
    sendData(data)

#Filtrerar bort angivet ssid från dataframe(obs måste innehålla wlan.ssid fältet som fås från ursprungs csvn)
def filterSSID(ssid, data): # data kommer att droppa alla rader som innehåller angivet ssid
    indexes = data[data['wlan.ssid'] == ssid].index
    data.drop(indexes, inplace=True)
    
def sendData(message):  #skickar data till server
    mySocket.sendall(message)

#skickar disconnect till servern och stänger ner våran socket.
def disconnect():
    mySocket.send(str.encode('disconnect'))
    mySocket.close()

# Väntar på att servern ska signalera start
def waitForStart(socket):
    data = socket.recv(1024).decode()
    if data == startStr:
        startAllThreads()
    else:
        print('error, implementera')

# Skapar trådkopplingen samt pipelinen för data capture, extraction och överföring till server
def startAllThreads():
    capture_thread = threading.Thread(target=captureAndSave, args=[5, 10000, 1])
    extraction_thread = threading.Thread(target=createCSVFromCapture)
    capture_thread.start()
    extraction_thread.start()

start_thread = threading.Thread(target = waitForStart, args = [mySocket])
start_thread.start()
### AVSLUTA PROGRAM
time.sleep(12)
end = True
### EGNA TANKAR 
# om transformeringen av data tar längre tid än caputring av packet kommer bottleneck problem att uppstå
# de tillfälliga filerna som skapas får jag inte glömma att ta bort efter(sparar atm för att se resultaten lättare)

"""
Kommunikation mellan datorer


När en klient disconnectar kommer den inte kunna återansluta, så att servern stänger connectionen om någon
tid har gått ifall klienten kraschat samt eventuellt också att vid medveten disconnect kanske informera
servern om det


-----------------------

Lokalisering av ankare

-----------------------

Grafiskt gränssnitt

----------------------

Eventuellt fingerprinting av alla datorer och signaler som vi använder vid behov


"""


