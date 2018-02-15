#!/usr/bin/env python3

import socket
import sys

HOST = ''   # Symbolic name meaning all available interfaces
PORT = 8888 # Arbitrary non-privileged port

# Datagram (udp) socket
try :
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print ('Socket created')
except socket.error as msg :
    print ('Failed to create socket. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
    sys.exit()


# Bind socket to local host and port
try:
    s.bind((HOST, PORT))
except socket.error as msg:
    print (b'Bind failed. Error Code : ' + msg[0] + b' Message ' + msg[1])
    sys.exit()

print ('Socket bind complete')

#now keep talking with the client
while 1:
    # receive data from client (data, addr)
    d = s.recvfrom(1024)
    data = d[0]
    addr = d[1]

    if not data:
        break

    reply = b'OK...' + data

    s.sendto(reply , addr)
    print ('Message[' + str(addr[0]) + '] - ' + str(data.strip()))

s.close()