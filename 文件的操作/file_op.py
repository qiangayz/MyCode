#coding=utf-8
import sys
import time
f = open("demo.txt") #打开文件，python3中可以加参数encoding = "utf-8"
#print (f.read())#文件光标会跳到最后
#f.write("我今天学习了吗")    #w表示写，r表示读，a表示追加,r+ 读写，w+写读，a+追加读，rb二进制文件读（网络传输）
#wb二进制写
"""
for i in range(5):
     print (f.readline())

for index,line in enumerate(f.readlines()):#下标和列表项，只适合读小文件
    print index,line
"""

#另一种文件迭代器
num = 0
for line in f:
    if num == 9:
        continue
    print line
    num +=1

print (f.tell())   #打印当前的指针位置
print (f.seek(0))   #移动光标
print (f.tell())
print (f.name)
print (f.flush())  #把书写的内容刷到硬盘上，适合实时写入文件

for i in range(50):
    time.sleep(0.1)
    sys.stdout.write("#")   #CMD界面简易的进度表
    sys.stdout.flush()

f.truncate(10)#从当前光标往后截断留下前面的
f.close()