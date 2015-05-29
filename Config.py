#!/usr/bin/env python
import sys
import ConfigParser

class MyConfig(object):
	fileName = None
	cofing = None
	def __init__(self, fileName):
		config = ConfigParser.ConfigParser()
		config.read(fileName)
		self.fileName = fileName

	def __del__(self):
		pass

	def getInt(self,section, option):
		if config:
			int(config.get(section, option))
		else:
			return False
		return True

	def getString(self, section, option):
		if config:
			str(config.get(section, option))
		else:
			return False
		return True

	def __write(self, section, option, value):		
		if config:
			config.set(section, option, value)
			config.write(open(self.fileName, "w"))
			return True
		return False

	def __addSection(self, section):
		if config:
			if config.has_section(section):
				return False
			config.add_section(section)
			cofnig.write(open(self.filename, "w"))
	def __getSections(self):
		if config:
			return config.sections()

		return False

	def __getOptions(self, section):
		if config:
			return config.options()
		return False		
	
if __name__ == "__main__":
	main()
	sys.exit()
