import pickle
import queue
import socket
import threading
import time

### GLOBALS

# noterbart: När ankarna connectar till servern sparas deras ip-adress och det index ankarna
# får antas vara konstant och används i andra listor för att representera olika ankare.
# notera också att Queues är trådsäkra och rekommenderade att använda i multithreading i python
# Listor är också trådsäkra, men data ändringar är inte, men eftersom Queues är trådsäkra
# antar jag att en lista av queues borde vara helt säker. Dock inte fullt testat. 

max_conns = 2 # ska vara 3 med alla ankare uppsatta
host = "0.0.0.0"
port = 5000
clientThreads = [] # kanske inte behövs
ipAdresses = []
dataQueues =  [queue.Queue()] * max_conns
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
            print('took data from both threads at ' + str(time.time()))
            print('queue 1: ')
            print(extracted_datas[0])
            print('queue 2: ')
            print(extracted_datas[1])
            print('--------------------------------------')
 
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
                        conn.close()
                        break
                except:
                    extracted_data = pickle.loads(packet)
                    dataQueues[indexFromIp(ip)].put(extracted_data)

### MAIN

def tain():
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
    
    
main_thread = threading.Thread(target = tain)
main_thread.start()
algorithm_thread()
#if __name__ == '__main__':
  #  Main()