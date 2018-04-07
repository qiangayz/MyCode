#coding=utf-8
"""
新式类与旧式类的一个有区别的地方，主要表现在多个类继承上，
新式类遵循的是广度优先，而旧式类遵循的是深度优先
python2中经典类按照深度优先继承的，
pyhton3中，经典类和新式都是按照广度优先继承的
"""

#class people:  #经典类
class people(object): #新式类

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def eat (self):
        print '%s is rating'%self.name

    def talk(self):
        print '%s is talking'%self.name

    def sleep(self):
        print '%s is sleeping'%self.name

class Relation(object):

    def make_friends(self,obj):
        print '%s like %s'%(self.name,obj)

class Man(people,Relation):

    def __init__(self,name,age,money):
        #people.__init__(self,name,age)
        super(Man,self).__init__(name,age)   #新式类写法
        self.money = money

    def play_game(self):
        print '%s is playing game'%self.name

    def sleep(self):
        people.sleep(self)    #重写父类方法
        print 'man is sleep'

class Woman(people,Relation):

    def song(self):
        print '%s is sing a song'%self.name

man = Man('zq','25','1500')
man.sleep()

class School(object):
    def __init__(self,name,addr):
        self.name = name
        self.addr = addr
        self.student =[]
        self.teacher =[]

    def enroll(self,stuobj):
        print 'service for%s'%stuobj.name
        self.student.append(stuobj)

class SchoolMember(object):
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex

    def tell(self):
        pass

class Teacher(SchoolMember):
    def __init__(self,name,age,sex,salary,course):
        super(Teacher,self).__init__(name,age,sex)
        self.salary = salary
        self.course = course

    def tell(self):
        print  '''info of teacher:%s' 
                 name: %s
                 age:%s
                 salary:%s
                 course:%s
               '''%(self.name,self.name,self.age,self.salary,self.course)

    def teach(self):
        print '%s is teaching '%self.name

class Student(SchoolMember):
    def __init__(self,name,age,sex,schoolid,course):
        super(Student, self).__init__(name,age,sex)
        self.id = schoolid
        self.course = course

    def tell(self):
        print  '''info of student:%s' 
                 name: %s
                 age:%s
                 id:%s
                 course:%s
               '''%(self.name,self.name,self.age,self.schoolid,self.course)
