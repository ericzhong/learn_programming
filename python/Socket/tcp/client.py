#!/usr/bin/env python

from socket import *

HOST = 'localhost'
PORT = 21567
BUFSIZE = 1024
ADDR = (HOST, PORT)

c = socket(AF_INET, SOCK_STREAM)
c.connect(ADDR)

while True:
    data = raw_input('> ')
    if not data:
        break
    c.send(data)
    data = c.recv(BUFSIZE)
    if not data:
        break
    print data

c.close()

