#coding=utf-8
import os
import socket

client = socket.socket()    #申明socket类型，同时生成socket连接对象
client.connect(('localhost',6969)) #传入元组,连接到服务端
while True:
    msg = raw_input("please input:").strip()
    if len(msg) == 0: continue
    client.send(msg)
    cmdsize  = client.recv(1024)   #接受命令内容的长度
    client.send('准备好了，可以发了')
    print '命令内容大小：',cmdsize,'######'
    received_size = 0
    received_data = b''
    while received_size < int(cmdsize):
        data = client.recv(1024)
        received_size += len(data)
        received_data += data
    else:
        print 'cmd res receive done...',received_size
        print received_data
    # data = client.recv(1024)
    # print 'recv:',data

client.close()