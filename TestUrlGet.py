#!/usr/bin/env python
#coding:utf-8
import urllib
param = urllib.urlencode({"name":"jinqiao"})
f = urllib.urlopen("http://localhost:8700?%s" % param)
print f.read()
