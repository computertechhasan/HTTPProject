import sys
from socket import *
import struct
##Declaring server values
serverIP = "127.0.0.1"
serverPort = 12000
dataLen = 1000000


##Creating the server socket
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind((serverIP, serverPort))
serverSocket.listen(1)
print("The server is listening on port: " + str(serverPort))

##Handling requests
while True:
    connectionSocket, address = serverSocket.accept()
    print("Socket created!")
    data = connectionSocket.recv(dataLen).decode()
    print("The client sent " + data)
    data = "Hi I'm alive"
    connectionSocket.send(data.encode())
    connectionSocket.close()

