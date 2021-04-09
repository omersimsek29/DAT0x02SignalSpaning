import numpy as np
import pandas as pd
import math
import os
from os.path import expanduser

# mina capture filer ligger under hem mappen därav
def createCSVFromCapture(captureFile, saveFile): #captureFile behöver vara .pcap och saveFile.csv
    home = expanduser("~")
    os.chdir(home)
    os.system('tshark -r ' + captureFile + '.pcap -o\'column.format:"Dport","%D","Protocol","%p"\' -T fields -E separator=, -E header=y -e wlan.da -e wlan.sa -e wlan.ssid -e wlan_radio.signal_dbm -e wlan.ra -e wlan.ta > ' + saveFile + '.csv')
createCSVFromCapture('testfil', 'wiresharkdata5')

wireshark_data = pd.read_csv('C:\\Users\\pennz\\Downloads\\wiresharkdata2.csv')
extracted_data = pd.DataFrame(columns=['source', 'signal strength', 'packets'])
for index, row in wireshark_data.iterrows():
    if (not pd.isna(wireshark_data.iloc[index]['wlan.ta'])) and (not (wireshark_data.iloc[index]['wlan.ta'] in extracted_data['source'].values)):
        nf = wireshark_data.loc[wireshark_data['wlan.ta'] == wireshark_data.iloc[index]['wlan.ta']]
        extracted_data = extracted_data.append({'source': wireshark_data.iloc[index]['wlan.ta'], 'signal strength': nf['wlan_radio.signal_dbm'].mean(), 'packets' : len(nf)}, ignore_index=True)
   
def filterSSID(ssid, data): # data kommer att droppa alla rader som innehåller angivet ssid
    indexes = data[data['wlan.ssid'] == ssid].index
    data.drop(indexes, inplace=True)
#nytest = filterSSID("Emils privata", wireshark_data)
