import sys
from socket import *
import struct

argv = sys.argv
rawInfo = argv[1]
##idx 0 holds address/hostname, 1 holds port, 2 holds filename
requestInfo = ["","",""]
fillIndex = 0
for char in rawInfo:
    if char == ":" or char == "/":
        fillIndex += 1
        continue
    else:
        requestInfo[fillIndex] += char
server = requestInfo[0]
port = int(requestInfo[1])
fileName = requestInfo[2]
count = 1000000

httpRequestContainer = "PUTHTTPREQUESTHERE"
data = "I'm alive."

clientSocket = socket(AF_INET, SOCK_STREAM)
print("Attempting to connect to " + server + " on port " + str(port) + ".")
clientSocket.connect((server,port))
print("Sending data to server")
clientSocket.send(data.encode())
dataEcho = clientSocket.recv(count)
print("The server responded " + dataEcho.decode())
clientSocket.close()






