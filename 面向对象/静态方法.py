#coding=utf-8

class Dog(object):
    '''
    类的描述
    '''

    def __init__(self,name):
        self.name = name
        self.__food = None

    @staticmethod     #实际上跟类没什么关系，单纯的函数，但是必须通过类名来调用
    def eat(food):
        print ('%s is eating %s'%('xiaohuang',food))

    @classmethod       #类方法，只能访问类变量，不能访问实例变量
    def talk(cls):
        print ('is talking')

    @property
    def age(self):      #属性方法：把一个方法变成一个静态属性，不能直接赋值，无法直接删除，无法直接附值
        print self.__food

    @age.setter
    def age(self,food):
        print ('%s is  age %s'%(self.name,food))    #改变属性方法的值
        self.__food = food
    @age.deleter
    def age(self):
        del self.__food

    def __call__(self):   #对象的再次调用 obj（）
        print '123'

    def __str__(self):   #打印对象的时候不会返回内存地址，会返回该方法的返回值
        return '12434'
    def __new__(cls,*args,**kwargs):
        print '5654765'
        return object.__new__(cls)

d = Dog('xianghuang')
d.eat('mianbao')
d.age   #属性方法调用
d.age = 'huangyou' #属性方法附值
d.age
del d.age    #属性方法删除
#print d.age
print Dog.__doc__#返回类的描述
print d.__module__ #返回实例创建的地方
print d.__class__ #返回类名
print Dog.__dict__ #打印类里面的所有属性，不包括实例属性
print d.__dict__#打印所有实例属性，不包括类属性
c = Dog('xiangbai')
print c

#把一个字典封装成实例
# d.__getitem__
# d.__setitem__
# d.__delitem__

#__new__   在实例化时候会执行，而且在init前执行，用来创建实例的
#类的另一种创建方式
def func(self):
    print 'hello word'
Foo = type('Foo',(),{'talk':func})

print type(type(type('123')))

#__metaclass__  #表示这个类是由谁来创建的
class Mytype(type):
    def __init__(self,what,bases=None,dict=None):  #第一步
        super(Mytype,self).__init__(what,bases,dict)

    def __call__(self,*args,**kwargs):                    #第二步
        obj = self.__new__(self,*args,**kwargs)         #第二步
        self.__init__(obj)

class Foo(object):
    __metaclass__ = Mytype

    def __init__(self,name):   #第四步
        self.name = name

    def __new__(cls,*args,**kwargs):
        return object.__new__(cls,*args,**kwargs)   #第三步

obj = Foo()