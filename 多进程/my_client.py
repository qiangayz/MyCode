import socket

client = socket.socket()
client.connect(('localhost',9000))
while True:
    data = raw_input('>>')
    client.send(data)
    data = client.recv(1024)
    print data
client.close()