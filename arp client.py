import socket
import os
serverAddressPort   = ("127.0.0.1", 20001)
bufferSize          = 1024
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)


while (True):
    msgFromClient = input("Enter the command:")
    bytesToSend = str.encode(msgFromClient)
    UDPClientSocket.sendto(bytesToSend, serverAddressPort)
   
    msgFromServer = UDPClientSocket.recvfrom(bufferSize)
    msg = "Server {}".format(msgFromServer[0].decode())

   
    if('Have' in msg):
    	break
    f=open('a.txt','r')
    print(f.read()) 	

UDPClientSocket.close()
