#coding=utf-8
import pika
import time
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='hellow1',#这里为什么会重新声明一个队列，是因为不确定是客户端先启动还是服务端先启动，所以先确认队列存在
                      durable=True) #防止rabbitmq服务器挂掉数据丢失了，队列持久化，durable只保存了队列，不保存队里里面的数据
def callback(ch,method,properties,body):  #回调函数
    print '收到消息：',body
    time.sleep(30)
    print '消息处理完毕：', body
channel.basic_consume(callback,queue='hellow1',
                      #no_ack=True  需要客户端确认，如果正在处理消息的时候客户端挂掉就会转到下一个客户端，会等待消息完整的处理完
                      )#如果收到消息就调用callback来处理消息
print '等待接收消息。。。。。'
channel.start_consuming()   #循环持续运行下去

#消息持久化