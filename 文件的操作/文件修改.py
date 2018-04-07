#coding=utf-8
f = open("demo.txt","r")
with open("demo.txt","r") as f:
    print f.read()

#with open(file1) as obj1, open(file2) as obj2:
"""
f_new= open("demonew.txt","w")
for line in f:
    if "你的光照" in line:
        line = line.replace("你的光照","abc")
    f_new.write(line)
f_new.close()
print open("demonew.txt","r").read()
"""

