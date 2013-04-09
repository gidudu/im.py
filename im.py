#!/usr/bin/python
#An instant messaging program implemented in Python.
#Created on Sunday, December 30, 2012

import thread
import socket
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def get_cli_msg():
	while True:
		r = s.recv(8192)
		
		if r == "\quit":
			s.close()
			sys.exit(0)
			
		print "\n" + sys.argv[1] + ": " + r + "\nYou: "
	
def get_serv_msg():
	while True:
		r = c.recv(8192)
		
		if r == "\quit":
			c.close()
			s.close()
			sys.exit(0)
			
		print "\n" + con_addr[0] + ": " + r + "\nYou: "

if sys.argv[1] == "-l":
	s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	s.bind(('', 5067))
	s.listen(5)
	c, con_addr = s.accept()
	thread.start_new_thread(get_serv_msg, ())
	
	while True:
		i = raw_input("You: \n")
			
		if i == "\quit":
			c.send("\quit")
			c.close()
			s.close()
			sys.exit(0)
		
		c.send(i)
else:
	s.connect((socket.gethostbyname(sys.argv[1]), 5067))
	thread.start_new_thread(get_cli_msg, ())
		
	while True:
		i = raw_input("You: \n")
		
		if i == "\quit":
			s.send("\quit")
			s.close()
			sys.exit(0)
			
		s.send(i)
