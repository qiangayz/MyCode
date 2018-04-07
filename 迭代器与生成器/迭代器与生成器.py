#coding=utf-8
"""
1、列表生成式
"""
list1 = [i for i in range(10)]
print list1
"""生成器 generator 只有在调用的时候才会生成相应的数值、只记录当前位置，
只有一个__next__方法.python2.7里面是next（）一般不用此方法，会使用for循环来遍历生成器

"""
list1 = (i for i in range(10))
print list1
#
#
# a= 1
# b=2
# a,b = b,a+b
# #相当于
# t = (b,a+b)
# a = t[0]
# b = t[1]

#生成器函数实例
def fib(value):
    i,j,z = 0,0,1
    while i < value:
        yield z
        j,z = z, j+z
        i +=1
#   return "end"   python2中不支持return


# fiber = fib(10)
# fiber.next()
# fiber.next()
# fiber.next()

#生成器并行的实例
import time
def consumer(name):
    print ("%s 准备"%name)
    while True:
        i = yield
        print ("%s is coming %s please ready"%(i,name))

a = consumer("liming")
a.next()
a.next()

def product():
    people1 = consumer("xiaoming")
    people2 = consumer("xiaohua")
    people1.next()
    people2.next()

    print ("接下来我准备发球了")
    for i in range(10):
        time.sleep(3)
        print ("发球了")
        people1.send("第"+str(i)+"颗球")
        people2.send("第"+str(i)+"颗球")

#product()
#可迭代的数据类型 列表 、元组、字典、集合、字符串 还有生成器，
#可迭代对象又称Iterable  可以使用isinstance判断一个对象是否是某个对象
#可以使用for循环遍历的对象称为可迭代对象，
#可以被next（）函数调用，并不断返回下一个值的对象称为迭代器 Iterator

from collections import Iterable,Iterator
print isinstance([],Iterable)   #判断迭代对象

isinstance([],Iterator)    #判断迭代器
print isinstance([i for i in range(10)],Iterator)
print isinstance((i for i in range(10)),Iterator)      #注意两个的区别

#把可迭代对象变成迭代器，之后就可以使用next（）函数了
i = iter([i for i in range(10)])
print "iter()函数",isinstance(i,Iterator)

list = [i for i in range(100) if i/2!=0]
print list
