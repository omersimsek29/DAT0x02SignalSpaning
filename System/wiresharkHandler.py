import numpy as np
import pandas as pd
import math
import threading
import os
import random
import string
import time
from os.path import expanduser

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

#Filtrerar bort angivet ssid från dataframe(obs måste innehålla wlan.ssid fältet som fås från ursprungs csvn)
def filterSSID(ssid, data): # data kommer att droppa alla rader som innehåller angivet ssid
    indexes = data[data['wlan.ssid'] == ssid].index
    data.drop(indexes, inplace=True)
#exempel
#nytest = filterSSID("Emils privata", wireshark_data)

### TRÅDAR 
semaphore = threading.Semaphore(0)
capture_thread = threading.Thread(target=captureAndSave, args=[5, 10000, 1])
extraction_thread = threading.Thread(target=createCSVFromCapture)
capture_thread.start()
extraction_thread.start()


### AVSLUTA PROGRAM
time.sleep(12)
end = True

### EGNA TANKAR 
# om transformeringen av data tar längre tid än caputring av packet kommer bottleneck problem att uppstå


