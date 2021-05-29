import sys
sys.path.append(".")
from RSSAlgorithm import targeted_positon
from RSSAlgorithm import targeted_positon2
import pickle
import queue
import socket
import threading
import time
import numpy as np
import MultiView as mw
import tkinter as tk 

### GLOBALS

# noterbart: När ankarna connectar till servern sparas deras ip-adress och det index ankarna
# får antas vara konstant och används i andra listor för att representera olika ankare.
# notera också att Queues är trådsäkra och rekommenderade att använda i multithreading i python
# Listor är också trådsäkra, men data ändringar är inte, men eftersom Queues är trådsäkra
# antar jag att en lista av queues borde vara helt säker. Dock inte fullt testat. 

max_conns = 3 # ska vara 3 med alla ankare uppsatta
host = "0.0.0.0"
port = 5000
clientThreads = [] # kanske inte behövs
ipAdresses = []
dataQueues =  [queue.Queue()] * max_conns
connections = []
discStr = 'disconnect'
startStr = 'start'
point1 = (0,0)
point2 = (3, 6.5)
point3 = (6,0)
frequency = 2422
listInExamRoom=[]
listdbm = []
results = []
root = tk.Tk() 


  

def inExamRoom(point): # Används inte, skulle användas för att avgöra om en uppsättning koordinater befann sig i tentasal eller ej
    if point[0] < 0 or point[0] > 6 or point[1] < 0 or point[1] > 6.5:
        return False
    else:
        return True 
# hårdkodning mellan ip-adress och koordinater för ankarna. 
def ipToPoint(ip):
    if ip == "192.168.1.101":
        return point1
    elif ip == "192.168.1.102":
        return point2
    elif ip == "192.168.1.100":
        return point3
# tänkt som en separat tråd som synkar algoritm beräkningar när servern mottagit data från alla
# ankare
def algorithm_thread():
    while True:
        emptyExist = False
        for index in range(len(dataQueues)):
            if dataQueues[index].empty(): # säkerställ att det finns data tillgänglig från alla ankare
                emptyExist = True
                break
        if not emptyExist: # om data finns från alla ankare
            extracted_datas = []
            for index in range(len(dataQueues)):
                extracted_datas.append(dataQueues[index].get()) # tar elementet som varit längst i kön från varje ankare
            for index in range(extracted_datas[0].shape[0]): # källan måste registrerats hos alla ankare för att vara relevant.
                shared_rows = []
                for row in extracted_datas:
                    shared_rows.append(row.loc[row['source'] == extracted_datas[0].iloc[index]['source']]) #plockar ut uppmätt signalstyrka för gemensam mac-adress
                if len(shared_rows) == max_conns: # måste finnas data hos alla ankare för att beräkna position
                    calculated_pos = (0,0)
                    for i in range(len(shared_rows)):
                        if len(shared_rows[0]['signal strength'].values) > 0 and  len(shared_rows[1]['signal strength'].values) > 0 and len(shared_rows[2]['signal strength'].values):
                            calculated_pos = targeted_positon(ipToPoint(ipAdresses[0]), ipToPoint(ipAdresses[1]), ipToPoint(ipAdresses[2]), shared_rows[0]['signal strength'].values[0], shared_rows[1]['signal strength'].values[0], shared_rows[2]['signal strength'].values[0], shared_rows[0]['frequency'].values[0]) # beräknar koordinater för signal
                        if not (calculated_pos == (0,0)) and (str(shared_rows[0]['source'].values[0]) =="56:80:d5:37:25:33" or str(shared_rows[1]['source'].values[0]) =="56:80:d5:37:25:33" or str(shared_rows[2]['source'].values[0]) =="56:80:d5:37:25:33"):                         
                            print(str(shared_rows[0]['source'].values[0]) + ' är beräknad att ligga på ' + str(calculated_pos) + ' och ' + str(inExamRoom(calculated_pos)))
                            results.append((shared_rows[0]['source'].values[0], calculated_pos)) # resultat lista för grafisk gränssnitt, sparas som (mac, koordinater)
                            listInExamRoom.append(inExamRoom(calculated_pos))
                            listdbm.append(shared_rows[0]['signal strength'].values[0]) # sparar signal styrkor för att kunna inspektera
                            listdbm.append(shared_rows[1]['signal strength'].values[0])
                            listdbm.append(shared_rows[2]['signal strength'].values[0])
                        #print('Signal strength of client : ' + str(i) + ' ' + str(shared_rows[i]['signal strength']))
                #shared_rows skickas sedan till algoritmen
            
# returnerar index för given ip-adress
def indexFromIp(ip):
    return ipAdresses.index(ip)

# funktion för hantering av ankar kommunikation mellan server och ett ankare i separat tråd.
def client_thread(conn, ip): #queue ska by default vara rekommenderat i multithreading och vara thread safe by default
    while True:
        if len(ipAdresses) == max_conns:
            packet = conn.recv(9192) # valde stor tillåten packet storlek för att undvika svårigheter med serializering
            if packet: 
                try: 
                    data = packet.decode() # kommer ge error om det är vår serializerade data och inte ett kommando
                    # Server kommandon placeras här
                    if data == discStr:
                        print('closing')
                        a = np.asarray(listdbm)
                        # b = np.asarray(listInExamRoom)
                        a.tofile('4.csv',sep=',',format='%10.5f')
                        # b.tofile('3.csv',sep=',',format='%10.5f')
                        conn.close()
                        break
                except: # kommer hit när serializerade data mottagits
                    extracted_data = pickle.loads(packet)
                    dataQueues[indexFromIp(ip)].put(extracted_data) # sparar i respektive ankares kö datan som mottagits

# funktion som används i en tråd för att hantera ankarnas anslutningar
def connection_thread():
    try:
        # standard anslutning med sockets
        data = []
        print (socket.gethostname())   
        mySocket = socket.socket()
        mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        mySocket.bind((host,port))    
        mySocket.listen(max_conns)
        while True:
            conn, addr = mySocket.accept()
            print ("Connection from: " + str(addr[0]))
            ipAdresses.append(addr[0])
            connections.append(conn)
            # skapar en ny tråd som hanterar anslutning mellan ett ankare och server
            clientConnection = threading.Thread(target=client_thread, args=[conn, addr[0]])
            clientConnection.start()
            clientThreads.append(clientConnection)
            # då rätt antal ankare anslutit till servern skickar servern ut ett start kommando till ankarna att starta avlyssning
            if(len(ipAdresses) == max_conns):
                for index in range(len(connections)):
                    connections[index].send(startStr.encode()) # skicka till alla enheter att det är dags att starta capture.
        conn.close()
    except KeyboardInterrupt:
        conn.close()
        
# Funktion som används för att dynamiskt uppdatera UI
def graphic_thread(): 
    view = mw.MainView(root) # nytt grafiskt gränssnitt
    view.pack(side="top", fill="both", expand=True)
    root.wm_geometry("400x400")
    updateUI(view)
    root.mainloop()
# Funktion som uppdaterar UI
def updateUI(view):
    if len(results) > 0:
        view.p4.print_result(results.pop(0))
    view.p4.after(1000, updateUI, view)  # läggs rekursivt till en update i tkinter varje sekund av grafiska gränssnittet, om data finns
        
### Trådstartning

main_thread = threading.Thread(target = connection_thread)
main_thread.start()
algoritm_thread = threading.Thread(target = algorithm_thread)
algoritm_thread.start() # var tänkt att vara main thread från början, men grafiskt gränssnitt krävde main, verkar dock inte leda till några buggar

graphic_thread() # graf tråd är tvungen att gå på "main thread"

