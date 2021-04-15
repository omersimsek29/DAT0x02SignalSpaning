import pickle
import threading
import socket

max_conns = 3
host = "0.0.0.0"
port = 5000

def client_thread(conn):
    while True:
        packet = conn.recv(4096)
        if packet: 
            extracted_data = pickle.loads(packet)
            print(extracted_data)

def Main():
    data = []
    print (socket.gethostname())

    mySocket = socket.socket()
    mySocket.bind((host,port))

    mySocket.listen(max_conns)
    while True:
        conn, addr = mySocket.accept()
        print ("Connection from: " + str(addr))
        clientConnection = threading.Thread(target=client_thread, args=[conn])
        clientConnection.start()
    conn.close()

if __name__ == '__main__':
    Main()