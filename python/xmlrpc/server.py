#!/usr/bin/python

import SimpleXMLRPCServer

class MyObject:
    def sayHello(self):
        return "XML-RPC OK!"

obj = MyObject()
server = SimpleXMLRPCServer.SimpleXMLRPCServer(("localhost", 8888))
server.register_instance(obj)

print "Listening on port 8888"
server.serve_forever()



