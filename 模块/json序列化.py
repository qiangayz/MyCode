import json
"""主要用于不同语言的数据公用 
"""
info = {"a":1,"b":3}
f = open("test.txt","w")
f.write(json.dump(info))
f.close()
data = json.load(f.read())   #只dump一次

print (__file__) #当前目录的相对路径
import os
print (os.path.abspath(__file__))    #返回绝对路径
 