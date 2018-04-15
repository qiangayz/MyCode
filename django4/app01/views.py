# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import redirect

# Create your views here.

def tpl(request):
    user_list = [1,2,3,4,5]
    return render(request,'tpl.html',{"u":user_list})

def tp2(request):
    name = 'root'
    return render(request,'tp2.html',{'name':name})

def tp3(request):
    status = '已经删除'
    return render(request,'tp3.html',{'status':status})

def master(request):
    return render(request,'master.html')

LISTDATA=['第%s个热补丁版本'%i for i in range(109)]
from django.utils.safestring import mark_safe

def hotVersionList(request):
    current_page = request.GET.get('p',1)
    current_page = int(current_page)
    start = (current_page-1) * 10
    end = current_page *10
    data = LISTDATA[start:end]
    all_count = len(LISTDATA)
    count,y =divmod(all_count,10)
    if y:
        count +=1
    page_list=[]
    for i in range(1,count+1):
        if i == current_page:
            temp = '<a class="active page" href="/hotVersionList/?p=%s">%s</a>'%(i,i)
        else:
            temp = '<a class="page" href="/hotVersionList/?p=%s">%s</a>'%(i,i)
        page_list.append(temp)
    print page_list
    pag_str=mark_safe("".join(page_list))
    print pag_str
    return render(request,'hotVersionList.html',{'li':data,'pag_str':pag_str})

user_info={
    'user':'user',
    'admin':'admin'
}
def login(request):
    if request.method == "GET":
        return render(request,'login.html')
    if request.method == "POST":
        u = request.POST.get('username')
        p = request.POST.get('password')
        dic = user_info.get(u)
        if not dic:
            return  render(request,'login.html')
        if u == 'user':
            res = redirect('/index/')
            res.set_cookie('username111',u)
            return res
        if u == 'admin':
            res = redirect('/index1/')
            res.set_cookie('username111', u)
            return res
        else:
            return render(request,'login.html')

def index(request):
    #获取当前已经登录的用户
    v = request.COOKIES.get('username111')
    if not v:
        return redirect('/login/')
    return  render(request,'index.html',{'current_user':v})

def index1(request):
    #获取当前已经登录的用户
    v = request.COOKIES.get('username111')
    if not v:
        return redirect('/login/')
    return  render(request,'index1.html',{'current_user':v})

def cookie(request):
    request.COOKIES
    request.COOKIES['username111']
    request.COOKIES.get('username111')