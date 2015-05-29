#!/usr/bin/env python

import sys
import os
import thread
import time


class MyThread(object):
    threadCount = 0
    runFlag = 0
    def start(self):
        thread.start_new_thread(self.startRun, (None, None))
        self.runFlag = 1

    def startRun(self, one, two):
        self.threadCount = self.threadCount+1
        self.run(one, two)
        self.threadCount = self.threadCount-1
        
    def run(self, one, two):
        pass

    def stop(self):
        self.runFlag = 0

    def getThreadStatus(self):
        if self.threadCount > 0:
            return True
        return False

    def getStopStatus(self):
        return self.runFlag

class MyThreadEx(object):
    threadCount = 0 
    runFlag = 0 
    def start(self, fun, one, two):
        thread.start_new_thread(run, (fun, two))
        self.runFlag = 1 

    def run(self, one, two):
        self.threadCount = self.threadCount+1
        one(None, None)
        self.threadCount = self.threadCount-1


    def stop(self):
        self.runFlag = 0 

    def getThreadStatus(self):
        if self.threadCount > 0:
            return True
        return False

    def getStopStatus(self):
        return self.runFlag



class MY(MyThread):
    name = "jinqiao"
    company = "lecai"
    age = 999
    def run(self, one, two):
        while True:
            if self.getStopStatus() == False:
                break
            print self.name, self.company, self.age
            time.sleep(1)


def t(a, b):
    print a, b
    while True:
        print time.time()
        time.sleep(1)




def main():
    
    mm = MY()
    mm.start()
    #thread.start_new_thread(t, ("one", "two"))
    while True:
        time.sleep(1)
        

if __name__ == "__main__":
    main()
    sys.exit()
