#!/usr/bin/env python
import sys
import thread
import time

class Lock(object):
	locki = None
	def __init__(self):
		self.locki = thread.allocate_lock()

	def lock(self):
		self.locki.acquire()

	def unlock(self):
		self.locki.release()

class AutoLock(object):
	locki = None
	def __init__(self, lock):
		self.locki = lock
		self.locki.lock()

	def __del__(self):
		self.locki.unlock()		
		

ll = Lock()
def fun(one, two):
	aa = AutoLock(ll)
	while True:
		print one, two
		time.sleep(1)	

def test(one, two):
	while True:
		print one, two
		time.sleep(1)
def main():	
	thread.start_new_thread(fun, (1, 2))
	thread.start_new_thread(fun, (111, 222))
	while True:
#		print time.time()
		time.sleep(1)
	
if __name__ == "__main__":
	main()
	sys.exit()
