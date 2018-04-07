#coding=utf-8
"""
1、定义
模块：用来从逻辑上组织python代码（变量、函数、类、逻辑。实现一个功能），本质就是.py结尾的python文件（对应的模块名不加.py）
包：本质一个目录，（必须带有一个__init__.py文件）。用来从逻辑上组织模块的
2、导入方法
import module_name
import mode1,mode2
from mode import *   会导入和当前文件内类似的方法，一般不建议使用
from mode import fumtion1 as funtion2
3、import本质
就是把python文件解释一遍
导入包的本质就是去解释文件夹下的初始化文件
4、导入优化
5、模块的分类
a、标准库
b、开源模块，第三方模块
c、自定义模块
"""

import sys,os
print sys.path
x = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) #导入其他路径的模块
sys.path.append(x)
#在包的__init__.py中导入模块
#from . import mode

#时间模块  time与datetime
import time
print time.time()  #   从1970年到现今的秒
print time.localtime()  #元组，当前时间
print time.strftime("%Y-%m-%d %H:%M:%S")
print time.asctime()
import datetime
print datetime.datetime.now()

#random模块
import random
print random.random()   #浮点型
print random.randint(1,3)
print random.randrange(10)
print random.choice("asdfasg")
print random.sample("asdfgdsgdfh",2)
list = [i for i in range(10)]
random.shuffle(list)
print list
print random.sample("asdfgdsgdfh",4)

#使用randon模块生成随机验证码
import random
code = ""
for i in range(5):
    cur = random.randrange(0,5)
    if cur == i:
        tmp=chr(random.randint(65,90))
    else:
        tmp = random.randint(0,9)
    code +=str(tmp)
print code