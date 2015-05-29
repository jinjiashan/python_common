#!/usr/bin/env python
#coding:utf-8
import sys
import os
def getRelaDir():
	try:
		if not file:
			raise "file is None"
		os.path.abspath(sys.argv[0])
		return os.path.dirname(sys.argv[0])	
	except Exception, e:
		print e

def main():
	print getRelaDir()
if __name__ == "__main__":

	main()
	sys.exit()
