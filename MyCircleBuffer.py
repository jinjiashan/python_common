#!/usr/bin/env python
#coding:utf-8
import os
import sys
import thread
class CircleBuffer(object):
    read = 0 
    write = 0 
    maxLen = 1024
    buffer = []
    def __init__(self, size=1024):
        self.maxLen = size
        self.buffer = [None for i in range(self.maxLen)]

    def push(self, data):
        len = self.getLen()
        if len >= self.maxLen-1:
            print "this is a full"
            return False

        self.buffer[self.write] = data
        self.write = (self.write + 1)%self.maxLen 
        print "push data=", data

    
    def pop(self):
        lenspa = self.getLen()
        if lenspa <= 0:
            print "this is a empty"
            return False
    
        data = self.buffer[self.read]
        self.read = (self.read + 1)%self.maxLen
        return data 

    def getLen(self):
        if self.write >= self.read:
            return self.write - self.read
        else:
            return self.maxLen - self.read + self.write
        

def test():
    ci = CircleBuffer(10)
    ci.push("oen")
    ci.push("two")
    ci.push("three")
    print ci.pop()
    print ci.pop()
    print ci.pop()
    print ci.pop()
    

if __name__ == "__main__":
    test()
    print "this is a my test for circlebuffer"
    sys.exit()