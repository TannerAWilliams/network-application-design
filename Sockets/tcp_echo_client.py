#!/usr/bin/env python3

"""
A simple echo client
"""

import socket

host = '192.168.1.108'
port = 50000
size = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host,port))
s.send(b'Hello, world')
data = s.recv(size)
s.close()
print ('Received:', data)