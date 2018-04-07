#coding=utf-8
import sys
## sys.argv #从命令行获取参数
import shutil
#文件、文件夹、压缩包、处理模块
f1 = open("test.txt")
f2 = open("test2.txt","wb")
#shutil.copyfileobj(f1,f2)
shutil.copyfile("test.txt","test2.txt")
shutil.copymode()#拷贝权限
shutil.copystat()#拷贝文件信息
shutil.copytree()#拷贝目录
shutil.rmtree()#删除目录
shutil.make_archive('文件名或路径','format格式','目标文件目录')#压缩
import zipfile

z = zipfile.ZipFile("one.zip",'w')  #压缩
z.write('test.txt')
z.close()

z = zipfile.ZipFile("one.zip",'r')  #解压
z.extractall()
z.close()

import shelve
d = shelve.open('mytest')
info = ["qa","b"]
d["info"] = info
d.get("info")