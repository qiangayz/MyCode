#coding=utf-8
'''
生成器就是一个简单的协程，微线程
遇到IO操作就切换
'''
# from greenlet import greenlet   #协程的手动切换 ，生成器属于自己开的一个协程，而greenlet是一个封装好的协程
# def test1():
#     print '12'
#     gr2.switch()
#     print '34'
# def test2():
#     print '56'
#     gr1.switch()
#     print '78'
#
# gr1 = greenlet(test1)   #启动一个协程
# gr2 = greenlet(test2)
# gr1.switch()

import gevent    #自动的协程切换，greenlet的包装版，主要针对IO操作
def foo():
    print '123'
    gevent.sleep(2)
    print('Explicit context switch to foo again')
def bar():
    print('Explicit精确的 context内容 to bar')
    gevent.sleep(1)
    print('Implicit context switch back to bar')
def func3():
    print("running func3 ")
    gevent.sleep(0)
    print("running func3  again ")


# gevent.joinall([
#     gevent.spawn(foo), #生成，
#     gevent.spawn(bar),
#     gevent.spawn(func3),
# ])


#gevent默认不知道urllib是io操作，所以需要加补丁
'''
python 3.x中urllib库和urilib2库合并成了urllib库， 
其中

urllib2.urlopen()变成了urllib.request.urlopen()
urllib2.Request()变成了urllib.request.Request() 
1
2
因此，python3.x得版本中可以使用urllib.request库； 
但是在python2.7的库中，还是得使用urllib2.urlopen
'''
# import urllib2
# #from urllib import re
# #import request
# import gevent,time
# from gevent import monkey
#
# monkey.patch_all()#把当前程序的所有io操作加入标记
# def f(url):
#     print 'now url is :%s'%url
#     resp = urllib2.urlopen(url)
#     data = resp.read()
#     print '%d bytes received from %s'%(len(data),url)
#
# urls = ['http://www.cnblogs.com/qiangayz/',
#         'http://www.cnblogs.com/qiangayz/p/8627979.html',
#         'http://www.cnblogs.com/qiangayz/p/8621020.html']
# time_start = time.time()
# for url in urls:
#     f(url)
# print '顺序执行花的时间:',time.time()-time_start
#
# timestart1 = time.time()
# gevent.joinall([
#     gevent.spawn(f,urls[0]),
#     gevent.spawn(f,urls[1]),
#     gevent.spawn(f,urls[2])
# ])
# print '协程异步花的时间：',time.time()-timestart1
#使用gevent实现socket多并发
# import sys
# import socket
# import time
# import gevent
#
# from gevent import socket, monkey
#
# monkey.patch_all()
#
#
# def server(port):
#     s = socket.socket()
#     s.bind(('0.0.0.0', port))
#     s.listen(500)
#     while True:
#         cli, addr = s.accept()
#         gevent.spawn(handle_request, cli)
#
#
# def handle_request(conn):
#     try:
#         while True:
#             data = conn.recv(1024)
#             print("recv:", data)
#             conn.send(data)
#             if not data:
#                 conn.shutdown(socket.SHUT_WR)
#
#     except Exception as  ex:
#         print(ex)
#     finally:
#         conn.close()


