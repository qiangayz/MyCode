#标准的函数体

def funtionname(x):
    """
    :param x:
    :return: 函数的说明，强烈建议写，养成良好的编程习惯
    """
    return x

#什么是面向过程编程，即将单个小的功能、顺序、逻辑、写到一个小函数里，再用多个小函数实现过程的逻辑的实现

def test1():
    print ("123")

def test2():
    return 0

def test3():
    return 1,2,["q","c","c"]

x = test1()           #函数1返回None，函数2返回object 1 函数三将所有元素放到一个元素里面返回，如果使用1个变量接受
y = test2()
z = test3()

#为什么会有返回值？想要函数的执行结果，后续逻辑需要判断此函数来决定是否执行

def funtionname(arg1,arg2):  #形参
    return arg1,arg2

funtionname(1,2)  #实参


#参数组
def funtionname(*args):  #参数返回为元组类型（必须接受位置参数）
    print args


def test_four(**kwargs):  #参数组传入字典的方式（关键字参数对位置无要求）
    print (kwargs)

test_four(a1="a",a2="b",a3="c")

#局部变量与全局变量  局部变量的作用域为函数，只在局部生效
#在局部更改全局的方法：global arg
#                       arg = value   不建议这么用，菜！


#全局变量 在函数顶层定义，可以函数内访问，但不可更改其值
#也可在函数内定义global arg
#                 arg = value  不建议这么定义，菜！！

#只有字符串，数字等不能在局部改全局，列表，字典、集合等可以在局部即函数里面更改全局


#递归函数 在函数内部调用自身 要求：1、必须有个明确的结束条件/2、问题规模必须比上次少 3、效率低

def calc(n): #对象最深调用次数999
    print (n)
    a = calc(n/2)
    return a

def calc1(n):
    print (n)
    if int(n/2)>0:
        return calc1(int(n/2))
    print ("->",n)

#高阶函数：将一个函数当做参数传给另一个参数
def add(a,b,f):
    return f(a)+f(b)

res = add(3,-6,abs)

#将字符串变为字典类型
list1 = ["a",1,"b",2,"c",3]
dict1 = eval(list1)















