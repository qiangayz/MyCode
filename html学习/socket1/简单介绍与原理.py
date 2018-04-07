#coding=utf-8
"""
HTML： 20个标签
        一套浏览器认识的规则
        学习规则。开发后台程序：写html文件
CSS ：颜色
      位置
html和CSS组成了基本的静态网页
和传统socket链接链接不同的是，传统的socket链接，连接之后就不会断开了，
而网页客户端链接之后获取到数据就会断开，在连接，再响应，再断开。俗称短链接。



一个基本的socket服务端：
"""
import socket
import time


def handle_request(client):
    buf = client.recv(1024)
    client.send("HTTP/1.1 200 OK\r\n\r\n")
    #client.send('hello ,word')   #html网页的源码实质上就是这个字符串
    #client.send("<h1 style='background-color:red;'>hello ,word<h1>") #增加一些格式
    f = open('index.html', 'rb') #可以把字符串放到文件里面，文件格式无所谓，一般默认为html后缀
    data = f.read()
    f.close()
    r = time.time()

    data = data.replace('@@@@@',str(r))   #可以把html文件当成一个模板，通过字符串替换的方式把变量写进源码中，
    # 当然这个变量可以是从数据库获取来的 有专门的web框架作为这个模板

    client.send(data)


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('localhost', 8000))
    sock.listen(10)

    while True:
        connection, address = sock.accept()
        handle_request(connection)
        connection.close()
if __name__ == '__main__':
    main()