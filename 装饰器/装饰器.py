#coding=utf-8
#装饰器本质为函数（用来装饰其他函数）为其他函数添加附加功能
#原则：1、不能修改被装饰函数的源代码
#2、不能修改函数的调用方式
#实现装饰器
#1、函数即变量
#2、高阶函数
#a、把一个函数名当做实参传入另一个函数
#b、返回值中包含函数名(不修改函数的调用方式)
#3、嵌套函数
#高阶函数+嵌套函数 = 装饰器

import time
#装饰器实例
# def timmer(func):
#     def warpper(*args,**kwargs):
#         start_time = time.time()
#         func()
#         stop_time = time.time()
#         print ("the funtion run time is %s"%(stop_time-start_time))
#     return warpper
# @timmer
# def fun1():
#     time.sleep(3)
#     print ("123456")
#
# fun1()
#
# def fun2():
#     print ("this is fun2")
#     fun3()

#匿名函数
# a = lambda x:x*3
# print a(3)

#高阶函数实例

# def fun1():
#     print ("123")
#
# def fun2(def1):
#     start_time = time.time()
#     time.sleep(3)
#     def1()
#     end_time = time.time()
#     print("fun run time is %s"%(start_time-end_time))
#
#
# fun2(fun1)   #调用fun1的一种方法加装饰的

# def fun3():
#     print ("456")
#
# def fun4(def1):
#     print time.time()
#     return def1
#
# x=fun4(fun3)
# x()
#
# fun3 = fun4(fun3)
# fun3()

#嵌套函数实例

# def fun5():
#     print ("this is fun 5")
#     def fun6():
#         print ("this is fun 6")
#     fun6()
#
# fun5()

def fun7():
    time.sleep(4)
    print ("this is fun7")

def fun8():
    time.sleep(6)
    print ("this is fun 8")

def deco(funname):                                     #只用到了高阶函数的第一个特性 把一个函数名当做实参传入另一个函数
    start_time = time.time()
    funname()
    end_time = time.time()
    print ("run time is %s"%(start_time-end_time))

# deco(fun7)                                           #此处给函数添加了新功能，但是调用方式变了
# deco(fun8)

def deco(funname):                                     #只用到了高阶函数的第二个特性 返回值中包含函数名(不修改函数的调用方式)可以实现不更改函数的调用方式
    start_time = time.time()
    return funname
    end_time = time.time()
    print ("run time is %s"%(start_time-end_time))
#
# fun7 = deco(fun7)
# fun7()                                               #此处调用方式没变但是没加入新功能
# fun8 = deco(fun8)
# fun8()

#接下来介入嵌套函数
# def fun9():
#     def fun10():
#         """
#         pass
#         :return:
#         """
#即
def fun9(funname):
    def fun10():
        start_time = time.time()
        funname()
        end_time = time.time()
        print ("run time is %s" % (start_time - end_time))
    return fun10

# fun7 = fun9(fun7)
# fun7()
#相当于
# @fun9
#  def fun7():
#         psss
@fun9    #这一步进行的操作就是执行fun7 = fun9(fun7)，而不会重新定义下面这个函数了
def fun7():
    time.sleep(4)
    print ("this is fun7")

#fun7()  #事实上执行的是fun10函数

@fun9
def fun11(time):
    print ("123")
#执行fun11,会报错
#fun11(1234)
#执行fun11相当于执行fun10所以可以在fun10上加参数
def fun9(funname):
    def fun10(*args,**kwargs):
        start_time = time.time()
        funname()
        end_time = time.time()
        print ("run time is %s" % (start_time - end_time))
    return fun10

user = "zte"
passw = "zte"

def ayth(arg1):
    print arg1
    def outweappen(funname):
        def wrapper(*args,**kwargs):
            username = raw_input("please input username: ").strip()
            password = raw_input("please in put password:").strip()
            if username ==user and passw == password:
                print("welcome")
                return funname(*args,**kwargs)

            else:
                exit()
        return wrapper
    return outweappen


@ayth
def index():
    print ("one")

@ayth
def home():
    print ("two")
    return "1241"  #这里需要返回值，因此要在wrapper内加入return funname（）

@ayth(arg1="abc")     #如果加了参数的话，就要使用多层嵌套
def blog():
    print ("thrree")
blog()
"""
@ayth(arg1="abc") 相当于blog = ayth（（arg1="abc"））=outweappen（）加了括号，相当于要执行outweappen函数，而此函数返回了wrapper
blog（） =  wrapper（）

"""