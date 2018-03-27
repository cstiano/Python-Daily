'''A sample of Python TCP server'''
# "{\"robot1\":{\"x\":1,\"y\":2,\"z\":0}, \"robot2\":{\"x\":0,\"y\":0,\"z\":0}, \"robot3\":{\"x\":0,\"y\":0,\"z\":0}, \"ball\":{\"x\":0,\"y\":0,\"z\":0}}"

import socket
import json

HOST = '127.0.0.1'        # Local host
PORT = 50007              # Arbitrary port

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)

print 'Waiting for connection...'
conn, addr = s.accept()

print 'Connected by client', addr
while 1:
	data = conn.recv(1024)
	if not data: break
	print 'Received data from client', repr(data), '...send it back...'
	d = json.loads(data)
	conn.send(data)

conn.close()
print 'Server closed.'