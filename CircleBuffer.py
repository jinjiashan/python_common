#!/usr/bin/env python
#coding:utf-8
import os
import sys


class CircleBuffer(object):
    read = 0 
    write = 0 
    maxLen = 1024
    buffer = []
    def __init__(self, size=1024):
        self.maxLen = size+1
        self.buffer = [None for i in range(self.maxLen)]
          
    def push(self, data):
       next = (self.write + 1)%self.maxLen
       if next != self.read:
           self.buffer[self.write] = data
           self.write = next
           return True
       return False
        
    def pop(self):
        data = None
        if self.read != self.write:
            data = self.buffer[self.read]
            self.read = (self.read+1)%self.maxLen
            return data
        return False
    
    def __getQueueLen(self):
        count = self.wriet - self.read
        if count < 0:
            count = count + self.maxLen
        return count

    def __getMaxLen(self):
        return self.maxLen -1
        
        


sys.path.append(os.path.dirname(sys.argv[0]))
import Thread
import time
class TestIn(Thread.MyThread):
	queue = None
	def __init__(self, bufferLen):
		self.queue = CircleBuffer(bufferLen)
        
	def run(self, one, two):
            while True:
                strData = "this is a time=" + str(time.time())
                if not self.queue.push(strData):
                    print "queue overflow"
                time.sleep(1)
            return False

class TestOut(Thread.MyThread):
	queue = None
	def __init__(self, que):
		self.queue = que

	def run(self, one, two):
            while True:
                startTime = time.time()
                while True:
                    data = self.queue.pop()
                    if data:
                        print "get result:", data
                    else:
                        break
                data = time.time() - startTime                 
                if data < 2:
                    time.sleep(2-data)
            return  None
				
def main():
    one = TestIn(1024)
    one.start()
    two = TestOut(one.queue)
    two.start()
    
    while True:
        time.sleep(1)
if "__main__" == __name__:
	main()
	sys.exit()
