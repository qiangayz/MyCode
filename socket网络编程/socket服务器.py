#coding=utf-8
#1、必须自己创建一个请求处理类，并且这个类要继承BaseRequesHandler，并且还要重写父类的handler方法
#2、必须实例化TCPServer，并且传递server IP 和第一不创建的请求处理类，给这个TCPServer当做参数传入
#3、server.handle_request() 只处理一个请求
#   server.serve_forever() 处理多个一个请求，永久执行

import SocketServer

class MyTcpHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        while True:
            try:
                self.data = self.request.recv(1024).strip()
                print '{} wrote:'.format(self.client_address)
                print self.data
                self.request.send(self.data.upper())
            except Exception as e:
                print 'error',e
                break


if __name__ == '__main__':
    Host,Port = 'localhost',9999
    server = SocketServer.ThreadingTCPServer((Host,Port),MyTcpHandler)   #ThreadingTCPServer多线程并发 TCPServer为单发的
    server.serve_forever()