#!/usr/bin/env python

from socket import *
from time import ctime

HOST = ''
PORT = 21567
BUFSIZE = 1024
ADDR = (HOST, PORT)

s = socket(AF_INET, SOCK_DGRAM)
s.bind(ADDR)

while True:
    print "waiting for message ..."

    data, addr = s.recvfrom(BUFSIZE)
    s.sendto('[%s] %s' % (ctime(), data), addr)

    print 'received from and returned to: ', addr

s.close()
