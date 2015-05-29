#!/usr/bin/env python
import sys
import MySQLdb 

def getData(con):
	cs = con.cursor()
	cs.execute("select one, two, three from two")

	while True:
		re = cs.fetchone()
		
		if not re:
			break		
		print re
	cs.close()

def setData(con):
	cs = con.cursor()
	try:
		print "start insert"
		sqlStr = "insert into two (one, two, three) values ('wo', 'shi', 'jinqiao')"
		cs.execute(sqlStr)
		con.commit()
	except Exception, e:
		print e
	cs.close()

def main():
	con = MySQLdb.Connection("127.0.0.1", "root", "lecai", "lecai")
	cs = con.cursor()
	getData(con)
	setData(con)
	con.close()
	
if __name__ == "__main__":
	main()
	sys.exit()
