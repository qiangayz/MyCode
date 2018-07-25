#coding=utf-8
class people(object):
    # def __init__(self):
    #     self.age = 45
    #     print('People')
    def sleep(self):
        print(123)

class Relation(object):
    def __init__(self):
        print('Relation')

class Man(people,Relation):
    def __init__(self):
        super(Man,self).__init__() #这里继承了两个类，但是只会执行people的构造方法，不会执行relation的，如果people没有构造函数就走relation
    def sleep(self):
        #people.sleep(self)
        super(Man,self).sleep()
        print(456)

# a = Man()
# a.sleep()
#深度优先于广度优先
"""
python2中经典类是深度优先，新式类是广度优先，python3中都是广度优先
"""
class A(object):
    def __init__(self):
        print('A')

class B(A):
    def __init__(self):
        print('B')

class C(A):
    def __init__(self):
        print('C')

class D(B,C):
    # def __init__(self):
    #     pass
    """
    深度优先：若D没有初始化函数，先去找B，B也没有去找A，A也没有再找C
    广度优先：若D没有初始化函数，先去找B，B也没有去找C，C也没有去找A
    """
