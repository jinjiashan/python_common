#!/usr/bin/env python
#coding:utf-8
import urllib
import urllib2
url = 'http://localhost:8700'
values = {"name":"jinqiao" }
data = urllib.urlencode(values)
print data
req = urllib2.Request(url, data)
response = urllib2.urlopen(req)
the_page = response.read()
print the_page
