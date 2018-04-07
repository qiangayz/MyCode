#coding=utf-8
import pika
import sys
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))  #建立socket连接可以加各种参数，端口，用户名，等
channel = connection.channel()  #声明一个管道

channel.exchange_declare(exchange='logs',exchange_type='fanout')   #声明一个队列
channel.basic_publish(exchange='logs',routing_key='',
                                   body = 'hellow,word',#队列的名字、消息内容

                                   )

print 'send hellow,word'
connection.close()