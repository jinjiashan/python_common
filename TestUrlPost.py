#!/usr/bin/env python
#coding:utf-8

import urllib
param = urllib.urlencode({"name":"jinqiao", "age":999})
print param
re = urllib.urlopen("http://localhost:8700/", param)
print re.read()
