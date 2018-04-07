#coding=utf-8
import paramiko
ssh = paramiko.SSHClient()
#允许链接不在linux上.ssh文件中不在known_hosts文件中的主机
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#链接服务器
ssh.connect(hostname='192.168.70.129',port=22,username='root',password='root' )
#执行命令
stdin,stdout,stder = ssh.exec_command('top -bn 1')
#获取命令结果
result = stdout.read()
print result
#关闭连接
ssh.close()

#在linux上生成私钥公钥的命令   ssh-keygen  存放路径root/.ssh/idrsa