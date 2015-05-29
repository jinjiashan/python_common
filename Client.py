#!/usr/bin/env python
#coding:utf-8

import sys
import socket
import time
import json
import copy

class Client(object):
    ip = None
    port = None
    sock = None
    def __init__(self, ip, port):
        try: 
            self.connect(ip, port)
        except Exception, e:
            print e
    def __del__(self):
        pass
    
    def connect(self, ip, port):
        try:
            if  ip and  port:
                self.ip = copy.deepcopy(ip)
                self.port = copy.deepcopy(port)
                self.sock = socket.socket()#copy.deepcopy(socket.socket())
                if self.sock:
                    self.sock.connect((self.ip, self.port))
        except Exception, e:
            print e
    
    def send(self, data):
        try:
            if not self.sock:
                return False
#                raise Exception("sock is None")
            self.sock.send(data)
        except Exception, e:
            print e
            
    def recv(self, len):
        try:
            if self.sock:
                return self.sock.recv(len)
        except Exception, e:
            print e
        return None
 
 
def main():
    cl = Client("127.0.0.1", 1112)
    
    while True:
        data = {"name":"leai", "id":999}
        dd = json.dumps(data)
        cl.send(dd)
        data = cl.recv(1024)
        print data
        time.sleep(1)  
 
if "__main__" == __name__:
    main()
    sys.exit()
