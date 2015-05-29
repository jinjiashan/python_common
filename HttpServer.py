#!/usr/bin/env python
#coding:utf-8
from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
class TestHTTPHandle(BaseHTTPRequestHandler):
    def do_GET(self):

        buf = "this is a test"

        self.protocal_version = "HTTP/1.1" 
	self.send_response(200)
	self.send_header("Welcome", "Contect")       	
	self.end_headers()
	
	
	self.wfile.write("client_address:"+ str(self.client_address)+"\n")
	self.wfile.write("command:"+str(self.command)+"\n")
	self.wfile.write("path:"+ str(self.path)+"\n")
	self.wfile.write("request_version:"+str(self.request_version)+"\n")
	self.wfile.write("headers:"+str(self.headers)+"\n")
	
	print self.path	
        self.wfile.write(buf)
    def do_POST(self):
	datas = self.rfile.read(int(self.headers['content-length']))
	print "data",  datas

        self.protocal_version = "HTTP/1.1" 
	self.send_response(200)
	self.send_header("Welcome", "Contect")       	
	self.end_headers()

	print "this is post", self.path

	self.wfile.write("WWWWWWWWWWWWWWWWWWWWWWWWWW")
	self.wfile.write("client_address:"+ str(self.client_address)+"\n")	
	self.wfile.write("command:"+str(self.command)+"\n")
	self.wfile.write("path:"+ str(self.path)+"\n")
	self.wfile.write("request_version:"+str(self.request_version)+"\n")
	self.wfile.write("headers:"+str(self.headers)+"\n")
def start_server(port):
    http_server = HTTPServer(("127.0.0.1", int(port)), TestHTTPHandle)
    http_server.serve_forever() #设置一直监听并接收请求


if __name__ == "__main__":
	start_server(8700)
