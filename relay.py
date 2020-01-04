import socket
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()

port = 5000

s.connect(('localhost', port))

relayNumber = sys.argv[1]
status = sys.argv[2]

sendString = "RELAY:" + relayNumber + ":" + status
print(sendString)
s.send(sendString.encode('ascii'))

s.close()
