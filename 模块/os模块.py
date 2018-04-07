#coding=utf-8
import os
os.getcwd() #获取目录
os.chdir(r'C:\user') #切换目录
os.curdir() #获取当前目录
os.pardir() #获取当前目录的父目录
os.makedirs(r'C:\a\b\v\d')  #创建目录
os.removedirs(r'C:\a\b\v\d') #目录为空则删除
os.mkdir() #单次创建
os.rmdir()#d单次删除
os.listdir()#列出当前目录下的文件及文件夹
os.remove() #删除文件
os.rename()#重命名文件
os.stat()#返回文件信息
os.sep()#输出当前操作系统的路径分隔符
os.linesep #输出当前平台的行终止符，win下为\t\n linux下为\n
os.pathsep #输出用于分割文件路径的字符串。环境变量中的分割符
os.environ #当前环境变量
os.system()#执行系统命令
os.path.abspath()#返回绝对路径
os.path.split()#分割目录和文件名
os.path.dirname()#返回path的路径名
os.path.basename()#返回path的文件名
os.path.exists()#判断路径是否存在
os.path.isabs()#是否是绝对路径
os.path.isfile()#是否文件
os.path.isdir()#是否为目录
os.path.join()#将多个路径组合返回
os.path.getatime()#返回最后存取时间
os.path.getmtime()#返回最后修改时间