#coding=utf-8
import os
import socket

client = socket.socket()    #申明socket类型，同时生成socket连接对象
client.connect(('localhost',9999)) #传入元组,连接到服务端
while True:
    msg = raw_input("please input:").strip()
    if len(msg) == 0: continue
    client.send(msg)
    cmdsize  = client.recv(1024)   #接受命令内容的长度

    print '命令内容大小：',cmdsize,'######'

client.close()