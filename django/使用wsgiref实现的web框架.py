#coding=utf-8
from wsgiref.simple_server import  make_server

def handle_fun1():
    f = open('test1.html',mode='rb')
    data = f.read()
    f.close()
    return data

def handle_fun2():
    return '<h1> hello func2</h1>'



DICT1 = {
    '/text1':handle_fun1,
    '/text2':handle_fun2
}
def Runserver(data,start_response):
    #data里面包含的是客户发来的所有数据
    #start_response 封装了要返回给用户的数据（响应头、状态等）
    start_response('200 OK', [("Content-Type", "text/html")])
    current_url =  data['PATH_INFO']
    print '====>',current_url
    func = None
    if current_url in DICT1:
        func = DICT1[current_url]
    if func:
        return func()
    else:
        return "404"
    #返回的内容

if __name__ == "__main__":
    httpobj = make_server('',8888, Runserver)
    print 'port HTTP on port 8888'
    httpobj.serve_forever()