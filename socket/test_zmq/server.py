# references
# https://linux.tips/programming/how-to-install-and-use-json-cpp-library-on-ubuntu-linux-os
# https://stackoverflow.com/questions/34600003/converting-json-to-string-in-python
# https://www.codeproject.com/Articles/1102603/Accessing-JSON-Data-with-Cplusplus
# https://stackoverflow.com/questions/31121378/json-cpp-how-to-initialize-from-string-and-get-string-value/31122041
# http://osdevlab.blogspot.com.br/2015/12/how-to-send-message-between-c-and.html
# https://www.codeproject.com/Articles/11843/Embedding-Python-in-C-C-Part-II 
# configurar ambiente de simulaçao, menos robos 

'''A sample of Python TCP server'''
# "{\"robot0\":{\"x\":1,\"y\":2,\"z\":0}, \"robot1\":{\"x\":0,\"y\":0,\"z\":0}, \"robot2\":{\"x\":0,\"y\":0,\"z\":0}, \"adv0\":{\"x\":0,\"y\":0,\"z\":0},\"adv1\":{\"x\":0,\"y\":0,\"z\":0},\"adv2\":{\"x\":0,\"y\":0,\"z\":0},\"ball\":{\"x\":0,\"y\":0,\"z\":0}}"
# "{\"robot0\":{\"left\":1,\"right\":2}, \"robot1\":{\"left\":0,\"right\":0}, \"robot2\":{\"left\":0,\"right\":0}}"
# "{\"robot0\":{\"x\":1,\"y\":2,\"z\":0}, \"robot1\":{\"x\":0,\"y\":0,\"z\":0}, \"robot2\":{\"x\":0,\"y\":0,\"z\":0}}"

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
	# d = json.loads(data)
	conn.send('{"robot0":{"left":100,"right":0},"robot1":{"left":100,"right":100},"robot2":{"left":0,"right":0} }')

conn.close()
print 'Server closed.'