import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

port = 5000
s.connect(('localhost', port))
sendString = "PROGRAM:ON"
s.send(sendString.encode('ascii'))
s.close()
