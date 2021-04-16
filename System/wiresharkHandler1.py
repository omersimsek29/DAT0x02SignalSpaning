import numpy as np
import pandas as pd
import math
import threading
import os
import random
import string
import time
from os.path import expanduser
import pickle
import queue
import socket

### GLOBALS

# noterbart: När ankarna connectar till servern sparas deras ip-adress och det index ankarna
# får antas vara konstant och används i andra listor för att representera olika ankare.
# notera också att Queues är trådsäkra och rekommenderade att använda i multithreading i python
# Listor är också trådsäkra, men data ändringar är inte, men eftersom Queues är trådsäkra
# antar jag att en lista av queues borde vara helt säker. Dock inte fullt testat. 

max_conns = 1 # ska vara 3 med alla ankare uppsatta
host = "0.0.0.0"
port = 5000
clientThreads = [] # kanske inte behövs
ipAdresses = []
dataQueues = [None] * max_conns
connections = []
discStr = 'disconnect'
startStr = 'start'

### FUNKTIONER

# funktion där position beräknas när algorithm tråden fått data från alla ankare. 
def algorithm(extracted_datas):
    print('calculate position')

# tänkt som en separat tråd som synkar algoritm beräkningar när servern mottagit data från alla
# ankare
def algorithm_thread():
    emptyExist = False
    while True:
        for index in range(len(dataQueues)):
            if dataQueues[index].empty():
                emptyExist = True
                break
        if not emptyExist:
            extracted_datas = []
            for index in range(len(dataQueues)):
                extracted_datas.append(dataQueues[index])
                algorithm(extracted_datas)
 
# returnerar index för given ip-adress
def indexFromIp(ip):
    return ipAdresses.index(ip)

# funktion för hantering av ankar kommunikation mellan server och ett ankare i separat tråd.
def client_thread(conn, ip): #queue ska by default vara rekommenderat i multithreading och vara thread safe by default
    while True:
        if len(ipAdresses) == max_conns:
            packet = conn.recv(4096)
            if packet: 
                try:    
                    data = packet.decode()
                    if data == discStr:
                        print('closing')
                        conn.close()
                        break
                except:
                    extracted_data = pickle.loads(packet)
                    if dataQueues[indexFromIp(ip)] == None:
                        q = queue.Queue()
                        q.put(extracted_data)
                        dataQueues[indexFromIp(ip)] = q
                    else:
                        dataQueues[indexFromIp(ip)].put(extracted_data)
                    print(extracted_data)

### MAIN

def Main():
    data = []
    print (socket.gethostname())

    mySocket = socket.socket()
    mySocket.bind((host,port))

    mySocket.listen(max_conns)
    while True:
        conn, addr = mySocket.accept()
        print ("Connection from: " + str(addr[0]))
        ipAdresses.append(addr[0])
        connections.append(conn)
        clientConnection = threading.Thread(target=client_thread, args=[conn, addr[0]])
        clientConnection.start()
        clientThreads.append(clientConnection)

        if(len(ipAdresses) == max_conns):
            for index in range(len(connections)):
                connections[index].send(startStr.encode()) # skicka till alla enheter att det är dags att starta capture.
    conn.close()

if __name__ == '__main__':
    Main()

### TSHARK KOMMANDON

#tshark -D för att se en lista av alla tillgängliga interfaces.

#kommando för att capturea och spara till test1.pcap, capture kommer att avbrytas när 1000 packet har captureats
# alternativt när en sekund gått.
#tshark -i 1 -w test1.pcap -a duration:1  -a packets:1000


### SETTINGS
pd.set_option("display.max_rows", None, "display.max_columns", None) # detta gör att man kan printa dataframes snyggt
home = expanduser("~")
os.chdir(home) # valt en dierctory för alla filer som är lätt att se. 

### GLOBALS
randomFilenameLength = 10
pcapFileNames = []
csvFileNames = []
end = False

### FUNKTIONER
#capturear och sparar med slumpmässigt namn som pcap
def captureAndSave(duration, packets, interfaceIndex):
    filename = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(randomFilenameLength))
    # säkerställ att airmon körs, om 0 packet captureas är det troligen pga det
    os.system('tshark -i' + str(interfaceIndex) + ' -w ' + filename + '.pcap -a duration:' + str(duration) + ' -a packets:' + str(packets))
    pcapFileNames.append(filename)
    semaphore.release()
    if end == False:
        captureAndSave(duration, packets, interfaceIndex)

#skapar en csv med samma namn som pcap filen med vissa intressanta fält enbart.
def createCSVFromCapture(): 
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

#Filtrerar bort angivet ssid från dataframe(obs måste innehålla wlan.ssid fältet som fås från ursprungs csvn)
def filterSSID(ssid, data): # data kommer att droppa alla rader som innehåller angivet ssid
    indexes = data[data['wlan.ssid'] == ssid].index
    data.drop(indexes, inplace=True)
#exempel
#nytest = filterSSID("Emils privata", wireshark_data)
"""
### TRÅDAR 
semaphore = threading.Semaphore(0)
capture_thread = threading.Thread(target=captureAndSave, args=[5, 10000, 1])
extraction_thread = threading.Thread(target=createCSVFromCapture)
capture_thread.start()
extraction_thread.start()


### AVSLUTA PROGRAM
time.sleep(12)
end = True
"""
### EGNA TANKAR 
# om transformeringen av data tar längre tid än caputring av packet kommer bottleneck problem att uppstå
# de tillfälliga filerna som skapas får jag inte glömma att ta bort efter(sparar atm för att se resultaten lättare)

"""
Kommunikation mellan datorer

Två möjliga alternativ, bluetooth och wifi.

Bluetooth verkar mer praktiskt, men verkar ha en sämre räckvid än vad wifi har som dessutom verkar vara på
gränsen till att vara för kort. Fördel med bluetooth är också att monitor mode verkar göra det i många fall
omöjligt att använda vanligt wifi, om en dator har bluetooth verkar det vara en annan interface som vi 
skulle kunna använda. 

Wifi verkar krångligare att använda, men har bättre range. På något sätt behöver vi antingen ha att våran
server broadcastar och berättar att den finns och att klienten då kan känna igen den alternativt att 
när en klient vill ansluta att den då skickar ut något "hello i'm here" och får sedan respons av servern.


-----------------------

Lokalisering av ankare

-----------------------

Grafiskt gränssnitt

----------------------

Eventuellt fingerprinting av alla datorer och signaler som vi använder vid behov


"""

