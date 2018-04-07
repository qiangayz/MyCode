#coding=utf-8
'''
原始的sql语句
CREATE TABLE user (
    id INTEGER NOT NULL AUTO_INCREMENT,
    name VARCHAR(32),
    password VARCHAR(64),
    PRIMARY KEY (id)

)
'''
#使用orm代码

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
engine = create_engine("mysql+pymysql://root:123456@192.168.70.129/my",   #建立数据库连接
                       encoding='utf-8', echo=False) #打印echo信息
Base = declarative_base()  # 生成orm基类
class User(Base):
    __tablename__ = 'user1'  # 表名
    id = Column(Integer, primary_key=True)
    name = Column(String(32))
    password = Column(String(64))

    def __repr__(self):
        return '%s name:%s' % (self.id, self.name)

class User2(Base):
    __tablename__ = 'user2'  # 表名
    id = Column(Integer, primary_key=True)
    name = Column(String(32))
    password = Column(String(64))

    def __repr__(self):
        return '%s name:%s'%(self.id,self.name)

Base.metadata.create_all(engine)  # base运行之后就会把继承他的所有子类表创建起来
#另一种不常用的创建方式
'''
from sqlalchemy import Table, MetaData, Column, Integer, String, ForeignKey
from sqlalchemy.orm import mapper
metadata = MetaData()
user = Table('user', metadata,
             Column('id', Integer, primary_key=True),
             Column('name', String(50)),
             Column('fullname', String(50)),
             Column('password', String(12))
             )
class User(object):
    def __init__(self, name, fullname, password):
        self.name = name
        self.fullname = fullname
        self.password = password
mapper(User,
       user)  # the table metadata is created separately with the Table construct, then associated with the User class via the mapper() function
'''
#————————————————————————增加————————————————————
from sqlalchemy.orm import sessionmaker   #操作表要导入这个模块
Session_class = sessionmaker(bind=engine)  # 创建与数据库的会话session class ,
# 注意,这里返回给session的是个class,不是实例，与数据库连接绑定bind=engine
Session = Session_class()  # 生成session实例 相当于pymysql里面的cursor
# user_obj = User(name="dzz", password="123456")  # 生成你要创建的数据对象
# user_obj1 = User(name="asd", password="123456")
# user_obj2 = User2(name="asd", password="123456")
# print(user_obj.name, user_obj.id)  # 此时还没创建对象呢，不信你打印一下id发现还是None
# Session.add(user_obj)  # 把要创建的数据对象添加到这个session里， 一会统一创建
# Session.add(user_obj2)
# Session.add(user_obj1)
#
# print(user_obj.name, user_obj.id)  # 此时也依然还没创建
# Session.commit()  # 现此才统一提交，创建数据
# print(user_obj.name, user_obj.id,user_obj.password)
#——————————————查询
data = Session.query(User2).filter_by(name = 'zq').all()   #返回一个列表,查一条
print '++>',data[0].name,data[0].password
print '++>',data

data = Session.query(User2).filter_by().all()    #在User2表的类里面加入了__repr__内置方法，就可显示了
print data

data = Session.query(User2).filter(User2.id>1).first() #单条，
print '>>',data

data = Session.query(User2).filter(User2.id>1).filter(User2.id<3).first()   #多条
print '>>',data

#修改——————————
data = Session.query(User2).filter(User2.id>1).filter(User2.id<3).first()   #多条件
print '>>',data
data.name = 'rest'
data.password = 'qqqqq'
Session.commit()
data = Session.query(User2).filter(User2.id>1).filter(User2.id<3).all()
print '>>',data
#回滚——————
user_obj4 = User2(name="zte", password="123456")
Session.add(user_obj4)
print '>>>#',Session.query(User2).filter(User2.name.in_(['zte'])).all()
Session.rollback()
print Session.query(User2).filter(User2.name.in_('zte')).all()
#分组统计
data = Session.query(User2).filter(User2.id>1).filter(User2.id<4).count()
print data

from sqlalchemy import func


#分组需要导入一个模块
data = Session.query(User2.name,func.count(User2.name)).group_by(User2.name).all()
print data

#连表查询
print Session.query( User2,User).filter(User2.id == User.id).all()
#print Session.query( User2).join(User).all()   #要求两个表有外键关联
#print Session.query( User2).join(User,isouter=True).all()