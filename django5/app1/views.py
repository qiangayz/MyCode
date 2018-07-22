# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect,HttpResponse

# Create your views here.
def login(request):
    if request.method == 'GET':
        return render(request,'login.html')
    if request.method == 'POST':
        u = request.POST.get('username')
        p = request.POST.get('pwd')
        check= request.POST.get('check')
        if u == 'root' and p =='123':
            """
            使用session之前需要先生成数据库
            1、生成随机序列
            2、将随机序列写到浏览器的cookie中
            3、将随机字符串保存到本地数据库的session中
            4、在随机字符串对应的字典设置相关内容
            默认时间为两周
            """
            request.session['username'] = u
            request.session['is_login'] = True
            if check:
                request.session.set_expiry(10)#主动设置超时时间
            return  redirect('/index/')
        else:
            return render(request,'login.html')


def index(request):
    if request.session.get('is_login'):
        return  render(request,'index.html',{'username':request.session.get('username')})
    else:
        return  HttpResponse('<h1>please login first</h1><a href="/login/">返回登录</a>')
    #return render(request,'index.html')

def logout(request):
    #del request.session['username']
    request.session.clear()
    return redirect('/login/')

def test(request):
    return HttpResponse('到此一游')


#——————————————————————form验证——————————————
from django import forms
from django.forms import widgets
from django.forms import fields
class FM(forms.Form):
    #第一种方式，最简版：
    # user = fields.CharField(
    # initial = 2,
    # widget = widgets.RadioSelect(choices=((1, '上海'), (2, '北京'),))
    #          )
    user = fields.CharField(error_messages={'required': '用户名不能为空.'},
                           widget=widgets.TextInput(attrs={'class':'c1'}), #定义插件，修改标签类型，CSS样式，属性等
                          label='用户名',
                          # initial='root',#默认值
                          help_text='这是帮助信息',
                            )
    pwd = fields.CharField(max_length=12,min_length=6,
                          error_messages={'required': '密码不能为空',
                                          'min_length':'密码长度不能小于6',
                                          'max_length':'密码长度不能大于12'},
                           widget=widgets.PasswordInput(attrs={'style':'background-color:blue;color:white'})
                           )
    email = fields.EmailField(error_messages={'required': '邮箱不能为空.','invalid':"邮箱格式错误"})
    f = fields.FileField()
    p = fields.FilePathField(path='app1')
    city = fields.ChoiceField(choices=[(0,'选项1'),(1,'选项2'),(2,'选项3'),])
    city1 = fields.MultipleChoiceField(choices=[(0,'选项1'),(1,'选项2'),(2,'选项3'),])
from app1 import models
def fm(request):
    if request.method == "GET":
        #生成默认值的方法：从数据获取数据
        dic={ "user":"r1",
        "pwd":"123123",
        "email":"3123",
        "city":"1",
        "city1":"2"}
        obj = FM(initial=dic)
        return render(request,'formtest.html',{'obj':obj})

    elif request.method == "POST":
        # 获取用户所有数据
        # 每条数据请求的验证
        # 成功：获取所有的正确的信息
        # 失败：显示错误信息
        obj = FM(request.POST)
        r1 = obj.is_valid()
        if r1:
            print obj.cleaned_data #返回正确信息
            models.Userinfo.objects.create(**obj.cleaned_data)
        else:
            print obj.errors #返回错误信息
            print obj.errors.as_json() #返回错误信息
            # print obj.errors['user'][0] #返回user的错误信息
        return  render(request,'formtest.html',{'obj':obj})

