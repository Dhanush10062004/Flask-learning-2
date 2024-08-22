import socket

c=socket.socket()
print('Client Socket created')

c.connect(('localhost',9998))
