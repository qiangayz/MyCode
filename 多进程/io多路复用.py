#coding=utf-8
#IO多路复用
#必须在非阻塞状态下才能使用socket的多路复用
import select
import socket
import sys
import Queue

sever = socket.socket()
sever.bind(('localhost',9000))
sever.listen(1000)

sever.setblocking(False)   #设置非阻塞模式
inputs = [sever]
outputs = []
msg_dict = dict()
while True:
    readable,writeable,exceptionable = select.select(inputs,outputs,inputs)   #检测到的链接放到inputs里面
    print readable,writeable,exceptionable
    for r in readable:
        if r is sever:
            con,addr=sever.accept()
            inputs.append(con)#因为新建立的链接没有发数据，因为是非阻塞，所以会出错，因此要把con加入select的监测列表
            print '有新的连接接入',con,addr
            msg_dict[con] = Queue.Queue()
        else:
            try:
                data = r.recv(1024)
                print '收到数据：',data
            except socket.error:
                print '客户端断开了：',
                inputs.remove(r)
                continue
            r.send(data)
            msg_dict[r].put(data)
            outputs.append(r)#放入返回的链接

    for w in writeable:    #要返回给客户端的了链接列表
        data1 = msg_dict[w].get()
        w.send(data1)    #返回给客户端数据
        outputs.remove(w) #确保斜刺循环的时候不返回已经处理的列表
    # sever.accept()
        for e in exceptionable:
            if e in outputs:
                outputs.remove(e)
            inputs.remove()
            del msg_dict[e]

#selector模块
import selectors
import socket

sel = selectors.DefaultSelector()


def accept(sock, mask):
    conn, addr = sock.accept()  # Should be ready
    print('accepted', conn, 'from', addr,mask)
    conn.setblocking(False)
    sel.register(conn, selectors.EVENT_READ, read) #新连接注册read回调函数，一调用read说明conn有数据接受了


def read(conn, mask):
    data = conn.recv(1024)  # Should be ready
    if data:
        print('echoing', repr(data), 'to', conn)  #repr？？
        conn.send(data)  # Hope it won't block
    else:
        print('closing', conn)
        sel.unregister(conn)
        conn.close()


sock = socket.socket()
sock.bind(('localhost', 9999))
sock.listen(100)
sock.setblocking(False)
sel.register(sock, selectors.EVENT_READ, accept)   #让select监听。回调函数accept。有活动就调此函数

while True:
    events = sel.select() #默认阻塞，有活动连接就返回活动的连接列表
    for key, mask in events:
        callback = key.data #accept
        callback(key.fileobj, mask) #key.fileobj=  文件句柄
