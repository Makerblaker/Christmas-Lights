#!/usr/bin/env python
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()

port = 5000

s.connect(('localhost', port))

sendString = "PROGRAM:OFF"
s.send(sendString.encode('ascii'))

s.close()
