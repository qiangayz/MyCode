#coding=utf-8
"""
abs() #取绝对值
all()#可迭代对象内全部元素为真则返回True，只要有一个非真，则返回False
any()#只要有一个真就为真，全非真则返回False
ascii()#把内存对象当做字符串打印出来
bin()#十进制转2进制
bool()#判断真假
callable()#判断能否调用
"""
# print (callable([1,2,2]))
# print callable(str)
# chr(97)
# print chr(97)
# ord() #与chr相反
# classmethod()#类方法
# compile()# 可以执行字符串类型的代码
code = """
for i in range(10):
    print i
"""
pyobj = compile(code,"error","exec")
exec(pyobj)                             #可以用来将代码当做字符串的方式传到远程电脑，然后执行代码用此方法
#直接exec（code）
delattr()
a = dict()
dir()#查找该对象的方法
divmod()#相除并返回余数
filter()  #从一组数据中过滤出想获得的数据
a = filter(lambda n:n>5,range(10))     #生成器
for i in a:
    print i
map()
b = map(lambda n:n*2,range(10))  #将range（10）里面每一项做操作之后返回
b = [lambda  n:n*2 for n in range(10)]
reduce()
reduce(lambda x,y:x+y ,range(10))#阶加
globals() #返回当前所有变量的key value 形式的字典
print globals()
hex()#转换为16进制
locals()#返回局部变量的值
oct()#转化为8进制
round()#保留两位小数
