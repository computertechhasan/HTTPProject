##Hasan Intisar
## hi6
## Section 002
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
##Normal Request
##httpRequestContainer = "GET " + fileName + " HTTP/1.1\r\n Host: " + server + ":" + str(port) + "\r\n\r\n" 
##IfModifiedRequest
httpRequestContainer = "GET " + fileName + " HTTP/1.1\r\nHost: " + server + ":" + str(port) + "\r\nIf-Modified-Since: Tue, 27 Mar 2018 16:06:02\r\n" 

clientSocket = socket(AF_INET, SOCK_STREAM)
print("Attempting to connect to " + server + " on port " + str(port) + ".")
clientSocket.connect((server,port))
print("The request being sent to the server is:\r\n" + httpRequestContainer)
clientSocket.send(httpRequestContainer.encode())
dataEcho = clientSocket.recv(count)
print(dataEcho.decode())
clientSocket.close()