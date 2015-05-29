#!/usr/bin/env python
import thread
import os
import sys
import json
import commands
import thread
import time
import twisted.internet.protocol
import twisted.internet.reactor

head = "he"
tail = "ta"
class Buffer(object):
    buffer = ""
    def getData(self):
        index = 0
        while True:
            temhead = self.buffer[index:index+2]
            if temhead == head:
                leng = len(self.buffer[index+2:index+2+2])
                if len(self.buffer[index:])  <= leng:
			self.buffer = self.buffer[index:]
                        return False
                else:
                        temtail = self.buffer[index+2+leng:2]
                        if temtail == tail:
                            ret = self.buffer[index+4:-2] 
                            self.buffer = self.buffer[index+6+leng:]
                            return ret
                        else:
                            index = index + 1

            else:
                index = index + 1

        self.buffer = self.buffer[index:]
        return False

    def appendData(self, data):
        self.buffer.append(data)

 

                

class Control(twisted.internet.protocol.Protocol):
    coned = {}
    count = 0
#    buffer = Buffer()
#    cirbu = CircleBuffer()
    def __init__(self):
        thread.start_new_thread(self.run, (None, None))
    def __del__(self):
        pass
    
    def run(self, one, two):
        while True:
            for key, value in self.coned.items():
                if  (time.time() - value[1]) > 8:
                    value[0].loseConnection()
                    print "print tiem:", value[1], time.time()

		time.sleep(1)
        
    def connectionMade(self):
        self.coned[self.transport.getPeer()] = [self.transport, time.time()]

    def connectionLost(self, reason):
	   key = self.transport.getPeer()
	   self.coned.pop(key)
	   print "this is a key lost:", key
	
    def dataReceived(self, data):
        print data
        self.updateTime()
        self.count = self.count + 1
        self.transport.write("this is a text:"+str(self.count))
    
    def updateTime(self):
        key = self.transport.getPeer()
        self.coned[key][1] = time.time()
        print "time update", self.coned[key][1], time.time()

class MyFactory(twisted.internet.protocol.Factory):
    data = "this is a pass"
    def one(self):
        pass


def startServer(one, two):
    fac =  MyFactory()

    fac.protocol = Control

    twisted.internet.reactor.listenTCP(one, fac)
    twisted.internet.reactor.run(installSignalHandlers=0)
    return True


if __name__ == "__main__":
   
    thread.start_new_thread(startServer, (1112, 333))
    while True:
        time.sleep(1)
        print "sleep:", time.time()

    sys.exit()
    
