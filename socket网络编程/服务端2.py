#coding=utf-8
#FTPserver
'''
1.读取文件名
2.检测文件是否存在
3.打开文件
4、检测文件大小
5、发送文件大小给客户端
6.等到客户端确认
7、开始边读边发数据
8、发送MD5
'''
import socket
import os
import hashlib

server = socket.socket()             #创建实例
server.bind(('localhost',6969)) #绑定要监听的端口
server.listen(2)  #开始监听

while True:          #第一层循环
    print '开始接听了'
    con1,addr =server.accept() #等连接接入,con1就是客户端连入，而在服务器端为其生成的连接实例
    print '%s is connect'%addr[0]
    while True:
        print '等待命令输入'
        try:
            data = con1.recv(1024)
            # if not data:
            #     print '%s 客户端断开了'%addr[0]
        except socket.error as e:
            print '%s 客户端断开了'%addr[0],e
            break
        print '执行指令:',data
        cmd,filename = data.split()
        print '要下载的文件是：',filename
        if os.path.isfile(filename):
            f = open(filename,'rb')
            m = hashlib.md5()
            file_size = os.stat(filename).st_size
            con1.send(str(file_size))
            con1.recv(1024)  #等待确认收到文件大小
            for line in f:
                m.update(line)
                con1.send(line)
            print '文件的MD5值:',m.hexdigest()
            f.close()
            con1.send(m.hexdigest())   #发送文件的MD5值
        print '传输文件完成了'
server.close()
