#!/usr/bin/env python

from socket import *
from time import ctime

HOST = ''
PORT = 21567
BUFSIZE = 1024
ADDR = (HOST, PORT)

s = socket(AF_INET, SOCK_STREAM)
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind(ADDR)
s.listen(5)

while True:
    print "waiting for connection ..."
    c, addr = s.accept()
    print 'connected from: ', addr

    while True:
        data = c.recv(BUFSIZE)
        if not data:
            break
        c.send('[%s] %s' % (ctime(), data))

    c.close()
s.close()
