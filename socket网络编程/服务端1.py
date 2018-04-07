#coding=utf-8
import socket
import os
import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')

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
        res = os.popen(data).read()
        print 'before send',len(res)

        if len(res) == 0:
            res = 'this cmd is error'
        con1.send(str(len(res)))
        client_ack = con1.recv(1024)  #等待服务端确认
        print '客户端收到了吗',client_ack
        con1.send(res)
        print '传输完成'
server.close()
