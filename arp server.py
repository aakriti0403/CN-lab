import socket
import subprocess
import os
localIP     = "127.0.0.1"
localPort   = 20001
bufferSize  = 1024


UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
UDPServerSocket.bind((localIP, localPort))
print("UDP server up and listening")


while(True):
    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
    message = bytesAddressPair[0]
    address = bytesAddressPair[1]
    clientMsg = "Message from Client:{}".format(message)
    clientIP  = "Client IP Address:{}".format(address)

    if('bye' in message.decode()):
    	UDPServerSocket.sendto("Have a nice day".encode(), address)
    	break

    os.system("arp -a "+message.decode()+'>a.txt')
    UDPServerSocket.sendto("Command executed".encode(), address)

UDPServerSocket.close()
