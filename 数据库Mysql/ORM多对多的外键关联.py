#coding=utf-8
from sqlalchemy import Table, Column, Integer,String,DATE, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
engine = create_engine("mysql+pymysql://root:123456@192.168.70.129/test1?charset=utf8",
                       encoding='utf-8', echo=False)

Base = declarative_base()

#这张表不会手动去维护，用户不需要关注，
book_m2m_author = Table('book_m2m_author', Base.metadata,
                        Column('book_id',Integer,ForeignKey('books.id')),
                        Column('author_id',Integer,ForeignKey('authors.id')),
                        )

class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer,primary_key=True)
    name = Column(String(64))
    pub_date = Column(DATE)
    authors = relationship('Author',secondary=book_m2m_author,backref='books') #secondary 意思是查找的时候通过book_m2m_author去查Author

    def __repr__(self):
        return self.name

class Author(Base):
    __tablename__ = 'authors'
    id = Column(Integer, primary_key=True)
    name = Column(String(32))

    def __repr__(self):
        return self.name

Base.metadata.create_all(engine)


#写入数据
Session_class = sessionmaker(bind=engine)
session = Session_class()
# b1 = Book(name="bbu1")
reload(sys)
sys.setdefaultencoding('utf-8')
b2 = Book(name=u"我的世界")
# b3 = Book(name="bbu3")
#
# a1 = Author(name="people1")
# a2 = Author(name="people2")
# a3 = Author(name="peo3ple")
#
# b1.authors = [a1, a2]
# b2.authors = [a1, a2, a3]
# b3.authors = [a1,a2,a3]
session.add_all([b2])
session.commit()

#查询
# obj = session.query(Author).filter( Author.name == 'people1').all()
# print obj[0].books
# book_obj = session.query(Book).filter( Book.id == 1).all()
# print book_obj[0].authors