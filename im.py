#!/usr/bin/python
#An instant messaging program implemented in Python by Jacob Dunefsky.
#Created on Sunday, December 30, 2012

import socket
import sys
import threading

def server_listen():
	while True:
		r = c.recv(8192)
		
		if r == "\quit":
			c.close()
			s.close()
			sys.exit(0)
		
		print con_addr[0], ": " + r

def client_listen():
	while True:
		r = s.recv(8192)
		
		if r == "\quit":
			s.close()
			sys.exit(0)
		
		print sys.argv[1], ": " + r

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

if sys.argv[1] == "-l":
	s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	s.bind(('', 5067))
	s.listen(5)
	c, con_addr = s.accept()
	
	while True:
		r = c.recv(8192)
		
		if r == "\quit":
			c.close()
			s.close()
			sys.exit(0)
		
		print con_addr[0], ": " + r
		i = raw_input("You: ")
		
		if i == "\quit":
			c.send("\quit")
			c.close()
			s.close()
			sys.exit(0)
		
		c.send(i)		
		
else:
	s.connect((socket.gethostbyname(sys.argv[1]), 5067))
	print "Chat initiated with " + sys.argv[1] + "!"
	
	while True:
		i = raw_input("You: ")
		
		if i == "\quit":
			s.send("\quit")
			s.close()
			sys.exit(0)
		
		s.send(i)
		r = s.recv(8192)
		
		if r == "\quit":
			s.close()
			sys.exit(0)
		
		print sys.argv[1] + ": " + r
