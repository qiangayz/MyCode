#coding=utf-8
import paramiko
transport = paramiko.Transport(('192.168.70.129',22))
transport.connect(username='root',password='root')
sftp = paramiko.SFTPClient.from_transport(transport)
sftp.put('test1.py','/tmp/test1.py')    #上传
sftp.get('/tmp/yum.log','yum.log')      #下载
transport.close()