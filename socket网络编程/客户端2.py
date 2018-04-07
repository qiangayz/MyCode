#coding=utf-8
import os
import socket
import hashlib

client = socket.socket()    #申明socket类型，同时生成socket连接对象
client.connect(('localhost',6969)) #传入元组,连接到服务端
while True:
    msg = raw_input("please input:").strip()
    if len(msg) == 0: continue
    if msg.startswith('get'):
        client.send(msg)                #发送命令
        cmdsize  = client.recv(1024)   #接受命令内容的长度
        cmdsize = int(cmdsize)
        client.send('准备好了，可以发文件了了')    #发送收到文件大小的信息
        print '命令内容大小：',cmdsize,'######'
        received_size = 0
        received_data = b''
        filename = msg.split()[1]
        f = open(filename + 'new','wb')
        m = hashlib.md5()
        while received_size < cmdsize:
            if cmdsize - received_size <= 1024:
                data = client.recv(cmdsize - received_size)
                print '最后一次剩多少了',cmdsize - received_size
            else:
                data = client.recv(1024)
            received_size += len(data)
            m.update(data)
            f.write(data)
        else:
            new_file_md5 = m.hexdigest()
            print '接受完成',received_size,'/',cmdsize
            f.close()
        server_file_md5 = client.recv(1024)
        print '服务器的MD5' ,server_file_md5
        print '客户端的MD5',new_file_md5
        # data = client.recv(1024)
        # print 'recv:',data

client.close()