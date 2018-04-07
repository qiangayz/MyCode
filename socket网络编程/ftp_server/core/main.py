#coding=utf-8
import SocketServer
import json
import os

class MyTcpHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        while True:
            try:
                self.data = self.request.recv(1024).strip()
                print '{} wrote:'.format(self.client_address)
                print self.data
                cmd_dict =  json.loads(self.data)
                action = cmd_dict['action']
                if hasattr(self,action):
                    funtion = getattr(self,action)
                    funtion(cmd_dict)
                self.request.send(self.data.upper())
            except Exception as e:
                print 'error',e
                break

    def put(self,*args):
        cmd_dict = args[0]
        filename = cmd_dict['filename']
        filesize = cmd_dict['size']
        if os.path.isfile(filename):
            f = open(filename+'new','wb')
        else:
            f = open(filename,'wb')
        self.request.send('可以上传了')
        received_size= 0
        while received_size < filesize:
            data = self.request.recv(1024)
            f.write(data)
            received_size += len(data)
        else:
            '文件上传完成'



if __name__ == '__main__':
    Host,Port = 'localhost',9999
    server = SocketServer.ThreadingTCPServer((Host,Port),MyTcpHandler)   #ThreadingTCPServer多线程并发 TCPServer为单发的
    server.serve_forever()