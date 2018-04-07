#coding=utf-8
class Dog(object):

    def __init__(self,name):
        self.name = name

    def eat(self):
        print '1234'

def talk(self):
    print '678678'
d = Dog('xiaobai')
#choice = raw_input('input:').strip()
#print (hasattr(d,choice))   #判断一个对象里是否有对应的字符串的方法映射
#getattr(d,choice)()          #根据字符串去获取对象里的对应的方法的内存地址
#setattr(d,choice,talk)        #给指定对象加一个方法  d.choice=talk
#d.talk(d)

#setattr(d,choice,22)             #给指定对象加一个实例变量
#print (getattr(d,choice))
#i = getattr(d,'eat')
# print (hasattr(d,'name'))
# delattr(d,'name')              #删除类变量
# d.name
i = 'eat1'
if hasattr(d,i):
    getattr(d,i)()
else :
    setattr(d,i,talk)
    func = getattr(d,i)
    func(d)

