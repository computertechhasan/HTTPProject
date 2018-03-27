##Hasan Intisar
## hi6
## Section 002
import sys
from socket import *
import struct
import datetime, time
import os.path
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
    requestHolder = data.split()
    print("The client sent the following request: " + data)
    ifModifiedSinceDateString = ""
    ##Parse for key info
    for index in range(0,len(requestHolder)):
        if requestHolder[index] == "GET":
            fileName = requestHolder[index+1]
        if requestHolder[index] == "If-Modified-Since:":          
            ifModifiedSinceDateString = requestHolder[index+1] + requestHolder[index+2] + " " + requestHolder[index+3] + " " + requestHolder[index+4] + " " + requestHolder[index+5]
    fileFailure = 0
    currTime = datetime.datetime.now()
    httpHeaderDate = currTime.strftime("%a, %d %b %Y %H:%M:%S %Z\r\n")
    ##Handle file not found
    try:
        with open(fileName) as webFile:
            fileContents = webFile.read()
    except:
        fileFailure = 1
    if fileFailure == 0:
        fileLastModifiedSecs = os.path.getmtime(fileName)
        if ifModifiedSinceDateString != "":
            ifModifiedSinceDate = datetime.datetime.strptime(ifModifiedSinceDateString,"%a,%d %b %Y %H:%M:%S")
            ifModifiedSinceDateSeconds = ifModifiedSinceDate.timestamp()
        if ifModifiedSinceDateString != "":
            if fileLastModifiedSecs > ifModifiedSinceDateSeconds:
                responseHeader = "HTTP/1.1 200 OK\r\nDate: " + str(httpHeaderDate) + "Content Length: " + str(len(fileContents)) + "\r\n" + "Content-Type: text/html; charset=UTF-8\r\n"
                responseMessage = responseHeader + fileContents
            else:
                responseMessage = "HTTP/1.1 304 Not Modified\r\nDate: " + str(httpHeaderDate) +"\r\n"
        else:
            responseHeader = "HTTP/1.1 200 OK\r\nDate: " + str(httpHeaderDate) + "Content Length: " + str(len(fileContents)) + "\r\n" + "Content-Type: text/html; charset=UTF-8\r\n"
            responseMessage = responseHeader + fileContents
    else:
        responseMessage = "HTTP/1.1 404 Not Found\r\nDate: " + str(httpHeaderDate) + "\r\n"
    connectionSocket.send(responseMessage.encode())
    connectionSocket.close()

