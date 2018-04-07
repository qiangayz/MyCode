#coding=utf-8
import pika
import time
connection = pika.BlockingConnection(pika.ConnectionParameters(host = 'localhost'))
channel = connection.channel()
channel.exchange_declare(exchange='logs',#这里为什么会重新声明一个队列，是因为不确定是客户端先启动还是服务端先启动，所以先确认队列存在
                      exchange_type='fanout') #直接加位置参数会出错,必须指定参数

result = channel.queue_declare(exclusive=True)#生成一个随机队列，用完之后删除
queue_name = result.method.queue

channel.queue_bind(exchange='logs',queue=queue_name)

def callback(ch,method,properties,body):  #回调函数
    print '收到消息：',body
    time.sleep(30)
    print '消息处理完毕：', body
channel.basic_consume(callback,queue=queue_name
                      #no_ack=True  需要客户端确认，如果正在处理消息的时候客户端挂掉就会转到下一个客户端，会等待消息完整的处理完
                      )#如果收到消息就调用callback来处理消息
print '等待接收消息。。。。。'
channel.start_consuming()   #循环持续运行下去

#消息持久化