import socket

s=socket.socket()
print("Socket Created")

s.bind(('localhost',9999))

s.listen(3)
print('Waiting for Connections')

while True :
    c,address=s.accept()
    print('Connected WIth the address',address)

    c.send(bytes('I am Dhanush'))

    c.close()



