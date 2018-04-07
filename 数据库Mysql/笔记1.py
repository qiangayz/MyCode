#coding=utf-8
'''
每个数据库都有一个或多个不同的API用于创建，访问，管理，搜索和复制所保存的数据。
1.数据以表格的形式出现
2.每行为各种记录名称
3.每列为记录名称所对应的数据域
4.许多的行和列组成一张表单
5.若干的表单组成database
关系型数据库：
Oracle
Mysql   免费开源
SqlServer
'''
import pymysql
conn = pymysql.connect(host='192.168.70.129',port=3306,user='root',passwd='123456',db='my') #创建连接
cursor = conn.cursor()  #创建游标
raw = cursor.execute("select * from rruinfo")   #执行sql语句，返回影响行数
print raw
row_1 = cursor.fetchone()  #取一条
row_1 = cursor.fetchmany(3)  #取3条
row_1 = cursor.fetchall()  #取全部
'''
注：在fetch数据时按照顺序进行，可以使用cursor.scroll(num,mode)来移动游标位置，如：
•cursor.scroll(1,mode='relative')  # 相对当前位置移动
•cursor.scroll(2,mode='absolute') # 相对绝对位置移动

'''
print row_1
effect_row = cursor.executemany("insert into rruinfo(rruname,len,age,updatetime)values(%s,%s,%s,%s)", [("1.1.1.11",11,1,1),("1.1.1.11",2,1,1)])
conn.commit()#使用executemany时候需要commit一下，不然不生效
new_id = cursor.lastrowid  # 获取最新自增ID
print raw
cursor.close() #关闭游标
conn.close()   #关闭连接

import pymysql
#conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123', db='t1')
# 游标设置为字典类型
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
#r = cursor.execute("call p1()")
raw = cursor.execute("select * from rruinfo")         #不好使
result = cursor.fetchone()
print '-----------------------------------'
print result
conn.commit()
cursor.close()
conn.close()