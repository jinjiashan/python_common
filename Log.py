#!/usr/bin/env python
import sys
import logging
import time
class MyLog(object):
	mymode = None
	def __init__(self):
		pass
	
	def init(self, level, name, mode):
		temLevel = None
		self.mymode = mode
		if level == "INFO":
			temLevel = logging.INFO
		elif level == "DEBUG":
			temLevel = logging.DEBUG
		elif level == "WARNING":
			temLevel = logging.WARNING
		elif level == "ERROR":
			temLevel = logging.ERROR
		elif level == "CRITICAL":
			temLevel = logging.CRITICAL
		else:
			pass

		logging.basicConfig(format="%(asctime)s %(levelname)s %(message)s",\
			 level=temLevel, filename=name,\
			 filemode="w",datefmt="%Y-%b-%d %H:%M:%S")

	def DEBUG(self, fmt, *data):
		self.output(fmt,  logging.debug, data)

	def INFO(self, fmt, *data):
		self.output(fmt,  logging.info, data)


	def WARNING(self, fmt, *data):
		self.output(fmt,  logging.warning, data)

	def ERROR(self, fmt, *data):
		self.output(fmt, logging.error, data)

	def CRITICAL(self, fmt, *data):
		self.output(fmt, logging.critical, data)	

	def output(self, fmt, fun, data):
		strDat = fmt % data
                if self.mymode & 1:
                        print strDat
                if self.mymode & 2:
                        fun(strDat)


if __name__ == "__main__":
	
	lll = MyLog()
	name = "jinqiao_"+str(time.time()) + ".log"
	
	lll.init("INFO", name, 3)
	
	while True:
		lll.WARNING("name %s company %s age %d, time %d", "jinqiao", "company", 9999, time.time())
		time.sleep(1)
	sys.exit()
