#!/usr/bin/python

import xmlrpclib

server = xmlrpclib.ServerProxy("http://localhost:8888")

ret = server.sayHello()

print ret
