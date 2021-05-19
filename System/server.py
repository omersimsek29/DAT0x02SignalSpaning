import os
#home = expanduser("~")
os.chdir(r"C:\Users\simse\OneDrive\Skrivbord\DAT0x02SignalSpaning-main\System")

import pickle
import queue
import socket
import threading
from math import log10
import time
import math
import numpy as np
import MultiView as mw
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
listCalculted = []
listInExamRoom=[]
listdbm = []

### KLASSER

class RSSAlgorithm:

    frequency = 0 
    point1 = (0,0)
    point2 =(0,0)
    point3 = (0,0)
    
    def __init__(self, frequency, point1, point2, point3):
        self.frequency = frequency
        self.point1 = point1
        self.point2 = point2
        self.point3 = point3



     
def distance_between_node_and_source(dbm,frequency):
    fspl = 27.55
    dist = 10 ** ((fspl -20* log10(frequency)+abs(dbm))/20)
    dist = round(dist,2)
    return dist


def targeted_positon(point1,point2,point3,dbm1,dbm2,dbm3,frequency):
    d1 = distance_between_node_and_source(dbm1,frequency)
    d2 = distance_between_node_and_source(dbm2,frequency)
    d3 = distance_between_node_and_source(dbm3 ,frequency)
    
    if point1.y<point2.y:
        y = point1.y+d1
    elif point1.y > point2.y:
        y = point2.y - d2
        
    else:
      x = point3.x-d3  
            
      return (x,y)
  
  
  
def targeted_positon2(point1,point2,point3,dbm1,dbm2,dbm3,frequency):
      
    d1 = distance_between_node_and_source(dbm1,frequency)
    d2 = distance_between_node_and_source(dbm2,frequency)
    d3 = distance_between_node_and_source(dbm3 ,frequency)
    
    a = (-2 * point1[0]) + (2*point2[0])
    b = (-2 * point1[1]) + (2*point2[1])
    d = (-2 * point2[0]) + (2*point3[0])
    e = (-2 * point2[1]) + (2*point3[1])
    
    c = (d1**2) - (d2 **2) - (point1[0]**2)+(point2[0]**2)-(point1[1]**2)+(point2[1]**2)
    f = (d2**2) - (d3 **2) - (point2[0]**2)+(point3[0]**2)-(point2[1]**2)+(point3[1]**2)
    
    x = ((c*e)-(f*b))/((e*a)-(b*d))
    y = ((c*d)-(a*f))/((b*d)-(a*e))
    
    return (x,y)

#rssAlg = RSSAlgorithm(2412, point1, point2, point3)
### FUNKTIONER

def distance_between_node_and_source(dbm,frequency):
    fspl = 27.55
    dist = 10 ** ((fspl -20* log10(frequency)+abs(dbm))/20)
    dist = round(dist,2)
    return dist

def targeted_positon2(point1,point2,point3,dbm1,dbm2,dbm3,frequency):
      
    d1 = distance_between_node_and_source(dbm1,frequency)
    d2 = distance_between_node_and_source(dbm2,frequency)
    d3 = distance_between_node_and_source(dbm3 ,frequency)
    
    a = (-2 * point1[0]) + (2*point2[0])
    b = (-2 * point1[1]) + (2*point2[1])
    d = (-2 * point2[0]) + (2*point3[0])
    e = (-2 * point2[1]) + (2*point3[1])
    
    c = (d1**2) - (d2 **2) - (point1[0]**2)+(point2[0]**2)-(point1[1]**2)+(point2[1]**2)
    f = (d2**2) - (d3 **2) - (point2[0]**2)+(point3[0]**2)-(point2[1]**2)+(point3[1]**2)
    
    x = ((c*e)-(f*b))/((e*a)-(b*d))
    y = ((c*d)-(a*f))/((b*d)-(a*e))
    
    return (x,y)

def targeted_positon(point1,point2,point3,dbm1,dbm2,dbm3,frequency):
    d1 = distance_between_node_and_source(dbm1,frequency)
    d2 = distance_between_node_and_source(dbm2,frequency)
    d3 = distance_between_node_and_source(dbm3 ,frequency)
    y=0
    x=0
    if point1[1] < point2[1]:
       
        y = point2[1] - d2
        x = point3[0] - d3  
        print("he1")

    elif point1[1] > point2[1]:
        y = point1[1] + d1
        x = point3[0] - d3  
        print("he2")
        
            
    return (x,y)

  

# funktion där position beräknas när algorithm tråden fått data från alla ankare. 
def algorithm(extracted_datas):
    print('calculate position')
def inExamRoom(point): #TODO
    if point[0] < 0 or point[0] > 6 or point[1] < 0 or point[1] > 6.5:
        return False
    else:
        return True 
# tänkt som en separat tråd som synkar algoritm beräkningar när servern mottagit data från alla
# ankare
def ipToPoint(ip):
    if ip == "192.168.1.101":
        return point1
    elif ip == "192.168.1.102":
        return point2
    elif ip == "192.168.1.100":
        return point3
def algorithm_thread():
    while True:
        emptyExist = False
        for index in range(len(dataQueues)):
            if dataQueues[index].empty():
                emptyExist = True
                break
        if not emptyExist:
            extracted_datas = []
            for index in range(len(dataQueues)):
                extracted_datas.append(dataQueues[index].get())
            #print('took data from both threads at ' + str(time.time()))
            #print('queue 1: ')
            #print(extracted_datas[0])
            #print('queue 2: ')
            #print(extracted_datas[1])
            #print('--------------------------------------')
            # kommentera ut antingen de printsen ovanför eller for looparna under för att enklare läsa vad som sker, dvs ha bara antingen eller aktiv
            for index in range(extracted_datas[0].shape[0]): # källan måste registrerats hos alla ankare för att vara relevant.
                shared_rows = []
                for row in extracted_datas:
                    shared_rows.append(row.loc[row['source'] == extracted_datas[0].iloc[index]['source']])
                if len(shared_rows) == max_conns:
                    calculated_pos = (0,0)
                    for i in range(len(shared_rows)):
                        if len(shared_rows[0]['signal strength'].values) > 0 and  len(shared_rows[1]['signal strength'].values) > 0 and len(shared_rows[2]['signal strength'].values):
                            print(str(ipToPoint(ipAdresses[0])) + ' = ip 1 ')
                            print(str(ipToPoint(ipAdresses[1])) + ' = ip 2 ')
                            print(str(ipToPoint(ipAdresses[2])) + ' = ip 3 ')
                            calculated_pos = targeted_positon(ipToPoint(ipAdresses[0]), ipToPoint(ipAdresses[1]), ipToPoint(ipAdresses[2]), shared_rows[0]['signal strength'].values[0], shared_rows[1]['signal strength'].values[0], shared_rows[2]['signal strength'].values[0], frequency) # ska vara en till med index 2 när alla ankare är anslutna
                        #print(shared_rows)
                        #print(shared_rows[0]['signal strength'].values[0])
                        #print('\n')
                        #print(shared_rows[1]['signal strength'])
                        #print(calculated_pos[0])
                        if not (calculated_pos == (0,0)) and (str(shared_rows[0]['source'].values[0]) =="56:80:d5:37:25:33" or str(shared_rows[1]['source'].values[0]) =="56:80:d5:37:25:33" or str(shared_rows[2]['source'].values[0]) =="56:80:d5:37:25:33"):                         
                            print(str(shared_rows[0]['source'].values[0]) + ' är beräknad att ligga på ' + str(calculated_pos) + ' och ' + str(inExamRoom(calculated_pos)))
                            listCalculted.append(calculated_pos)
                            listInExamRoom.append(inExamRoom(calculated_pos))
                            listdbm.append(shared_rows[0]['signal strength'].values[0])
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
            packet = conn.recv(9192)
            if packet: 
                try: # alla sträng kommandon servern kan hantera ska vara här
                    data = packet.decode()
                    if data == discStr:
                        print('closing')
                        a = np.asarray(listdbm)
                       # b = np.asarray(listInExamRoom)
                        a.tofile('4.csv',sep=',',format='%10.5f')
                       # b.tofile('3.csv',sep=',',format='%10.5f')
                                

                        conn.close()
                        break
                except:
                    extracted_data = pickle.loads(packet)
                    dataQueues[indexFromIp(ip)].put(extracted_data)

### MAIN

def connection_thread():
    try:
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
            clientConnection = threading.Thread(target=client_thread, args=[conn, addr[0]])
            clientConnection.start()
            clientThreads.append(clientConnection)
    
            if(len(ipAdresses) == max_conns):
                for index in range(len(connections)):
                    connections[index].send(startStr.encode()) # skicka till alla enheter att det är dags att starta capture.
        conn.close()
    except KeyboardInterrupt:
        conn.close()
        
        
mw.start_View()
main_thread = threading.Thread(target = connection_thread)
main_thread.start()
algorithm_thread()
#if __name__ == '__main__':
  #  Main()
