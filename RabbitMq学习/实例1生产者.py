#coding=utf-8
import pika
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))  #建立socket连接可以加各种参数，端口，用户名，等
channel = connection.channel()  #声明一个管道
channel.queue_declare(queue='hellow1',durable=True)   #声明一个队列
channel.basic_publish(exchange='',routing_key='hellow1',
                                   body = 'hellow,word',#队列的名字、消息内容
                                   properties=pika.BasicProperties(
                                       delivery_mode=2, )        #使消息持久化，服务器挂了不会丢失队里里面的消息
                                   )
print 'send hellow,word'
connection.close()