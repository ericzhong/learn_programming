#!/usr/bin/env python

from socket import *

HOST = 'localhost'
PORT = 21567
BUFSIZE = 1024
ADDR = (HOST, PORT)

c = socket(AF_INET, SOCK_DGRAM)

while True:
    data = raw_input('> ')
    if not data:
        break
    c.sendto(data, ADDR)
    data, ADDR = c.recvfrom(BUFSIZE)
    if not data:
        break
    print data

c.close()

