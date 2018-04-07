#coding=utf-8
from sqlalchemy import create_engine
from sqlalchemy import Integer, ForeignKey, String, Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

engine = create_engine("mysql+pymysql://root:123456@192.168.70.129/test1?charset=utf8",
                       encoding='utf-8', echo=False)

Base = declarative_base()

class Customer(Base):
    __tablename__ = 'customer'
    id = Column(Integer, primary_key=True)
    name = Column(String(64))
    billing_address_id = Column(Integer, ForeignKey("address.id"))
    shipping_address_id = Column(Integer, ForeignKey("address.id"))
    # billing_address = relationship("Address")
    # shipping_address = relationship("Address")
    billing_address = relationship("Address", foreign_keys=[billing_address_id])
    shipping_address = relationship("Address", foreign_keys=[shipping_address_id])

class Address(Base):
    __tablename__ = 'address'
    id = Column(Integer, primary_key=True)
    street = Column(String(64))
    city = Column(String(64))
    state = Column(String(64))

    def __repr__(self):
        return '(%s name: %s %s)'%(self.street,self.city,self.state)
Base.metadata.create_all(engine)
#___插入数据
from sqlalchemy.orm import sessionmaker,relationship
Session_class = sessionmaker(bind=engine)
session = Session_class()
# a1 = Address(street = 'nanfang',city = 'shanghai',state = 'china')
# a2 = Address(street = 'beifang',city = 'xian',state = 'china')
# a3 = Address(street = 'dongfang',city = 'shandong',state = 'china')
# a4 = Address(street = 'xifang',city = 'tianzhu',state = 'china')
# session.add_all([a1,a2,a3,a4])
#
# c1 = Customer(name= 'xiaohong',billing_address= a1,shipping_address  = a2 )   #python3里面可以直接billing_address_id = a1
# c2 = Customer(name = 'xiaohua',billing_address = a2,shipping_address  = a1)
# c3 = Customer(name = 'xiaoqiang',billing_address = a3,shipping_address  = a4)
# c4 = Customer(name = 'xiaofang',billing_address = a1,shipping_address  = a1)
# session.add_all([c1,c2,c3,c4])
# session.commit()

obj = session.query(Customer).filter( Customer.name == 'xiaohong').first()
print obj.name,obj.billing_address,obj.shipping_address
