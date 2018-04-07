#coding=utf-8
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String,DATE,ForeignKey
from sqlalchemy.orm import sessionmaker,relationship


engine = create_engine("mysql+pymysql://root:123456@192.168.70.129/test1",   #建立数据库连接
                       encoding='utf-8', echo=False) #打印echo信息
#写中文的方式
#engine = create_engine("mysql+pymysql://root:123456@192.168.70.129/test1？charser=utf8",
#                       encoding='utf-8', echo=False)
Base = declarative_base()  # 生成orm基类

class Student(Base):
    __tablename__ = 'student'
    id = Column(Integer,primary_key =True )
    name = Column(String(32),nullable= False)
    update_time = Column(DATE,nullable =False)

    def __repr__(self):
        return '(%s name: %s)'%(self.id,self.name)

class StudyRecord(Base):
    __tablename__ = 'study_record'
    id = Column(Integer,primary_key= True)
    day = Column(Integer,nullable=False)
    status = Column(String(32),nullable=False)
    stu_id = Column(Integer,ForeignKey('student.id'))  #w外键创建完成
    #study_obj = query（id= 1）
    #student = query(Student).filter(Student.id == stu_obj.stu_id).first()
    student = relationship('Student',backref = 'my_study_record')     #StudyRecord可以通过调用Student。
                                                                         # student中可以通过my_study_record查到StudyRecord里面的内容
    def __repr__(self):
        return '(%s name: %s)'%(self.id,self.day)

Base.metadata.create_all(engine)

Session_class = sessionmaker(bind=engine)
session = Session_class()
# s1 = Student(name = 'zq',update_time = '2018-01-01')
# s2 = Student(name = 'xiaohong',update_time = '2018-01-01')
# s3 = Student(name = 'xiaoming',update_time = '2018-01-01')
# s4 = Student(name = 'xiaohua',update_time = '2018-01-01')
# study_obj1 = StudyRecord(day = 1,status = 'YES',stu_id =1 )
# study_obj2 = StudyRecord(day = 2,status = 'YES',stu_id =1 )
# study_obj3 = StudyRecord(day = 3,status = 'NO',stu_id =1 )
# study_obj4 = StudyRecord(day = 1,status = 'YES',stu_id =2)
#session.add_all([s1,s2,s3,s4,study_obj1,study_obj2,study_obj3,study_obj4])   #pyhton中不能同时创建，会出错
#第二个表的id不是从1开始得，为什么？
#session.add_all([s1,s2,s3,s4])
# session.add_all([study_obj1,study_obj2,study_obj3,study_obj4])
# session.commit()
stuobj = session.query(Student).filter(Student.name=='zq').first()
print stuobj.my_study_record
