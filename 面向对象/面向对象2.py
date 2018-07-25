#coding=utf-8
"""
实例的变量又叫类的静态属性
类的方法又叫类的动态属性

类变量与实例变量的区别
x不用实例化就可以调用
所有实例都可以调用x
"""
class role():
    x = "1234"
    x_list =['123']
    def __init__(self,name):
        self.x = 6666
        self.name = name

    def __del__(self):
        print('woqule')

print role.x
print role("zq").x
#可以在外面给实例加属性，也可以删除或者修改,可以更改对象1的类变量（实际上实在对象1的内存里面增加和类变量同名的实例变量而已），但是不会更改其他实例的类变量
#可以通过role.x = '3434'来更改
r1 = role('zq')
r1.x_list=12312
r1.year = "25"
r1.name = "zqq"
print r1.year,r1.name
print r1.x_list,role.x_list
del r1
print(11111111111111)
"""
析构函数：收尾工作，关闭数据连接，打开的文件等
def __del__(self):
    print "1234"
    
私有属性：
在属性名前面加__
即：self.__name= name
在外面不可访问此属性，内部可以访问，可以通过在类里面建立函数return此属性来返回属性值，但是不可以修改
私有方法：
def __funtion()

"""