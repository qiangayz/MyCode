#coding=utf-8
import sys
s = "你好啊"

print type(s)
print (sys.getdefaultencoding())
s1 = s.decode("utf-8")   #从utf-8转换为unicode
s2= s1.encode("gbk")     #从unicode转换为gbk
print type(s2)
print s1,s2