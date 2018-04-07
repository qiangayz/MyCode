#coding=utf-8
import os
import socket
import hashlib
import json

# client = socket.socket()    #申明socket类型，同时生成socket连接对象
# client.connect(('localhost',6969)) #传入元组,连接到服务端
class FtpClient(object):
    def __init__(self):
        self.client = socket.socket()

    def help(self):
        """
        ls:
        pwd:
        cd..
        get filename
        put filename
        :return:
        """
    def connect(self,ip,port):
        self.client.connect((ip,port))

    def interactive(self):
 #       self.authenticate()
        while True:
            cmd = raw_input('>>').strip()
            if len(cmd) == 0 :continue
            cmd_str = cmd.split()[0]
            if hasattr(self,'cmd_%s'%cmd_str):
                func = getattr(self,'cmd_%s'%cmd_str)
                func(cmd)
            else:
                self.help()

    def cmd_put(self,*args):
        cmd_split = args[0].split()
        if len(cmd_split) >1 :
            filename = cmd_split[1]
            if os.path.isfile(filename):
                filesize = os.stat(filename).st_size
                msg_dic = {'action':'put',
                           'filename':filename,
                           'size':filesize}
                self.client.send(json.dumps( msg_dic))
                server_response = self.client.recv(1024)
                f = open(filename,'rb')
                for line in f:
                    self.client.send(line)
                else:
                    print '文件上传完成'
            else:
                print '文件不存在',filename

if __name__ == '__main__':
    ftp = FtpClient()
    ftp.connect('localhost',9999)
    ftp.interactive()