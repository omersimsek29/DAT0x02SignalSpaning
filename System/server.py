import pickle

import socket

def Main():
    host = "0.0.0.0"
    port = 5000
    data = []
    print (socket.gethostname())

    mySocket = socket.socket()
    mySocket.bind((host,port))

    mySocket.listen(1)
    conn, addr = mySocket.accept()
    print ("Connection from: " + str(addr))
    while True:
        packet = conn.recv(4096)
        extracted_data = pickle.loads(packet)
        print(extracted_data)
        if not packet: break
    conn.close()

if __name__ == '__main__':
    Main()