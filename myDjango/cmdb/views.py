# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import redirect

# Create your views here.
from django.shortcuts import HttpResponse

import time

# def home(request):
#     f=open('E:\myDjango\myDjango\login.html','rb')
#     data = f.read()
#     print data
#     return HttpResponse(data)
USER_LIST=[
    {'username':"zq",'email':"213","gender":"男"},
    {'username':"qwe",'email':"213","gender":"男"},
]
def home(request):
    if request.method=="POST":
        u = request.POST.get('username')
        e = request.POST.get('email')
        g = request.POST.get('gender')
        temp = {'username':u,'email':e,"gender":g}
        USER_LIST.append(temp)
    return render(request, 'home.html', {'user_list': USER_LIST})


def login(request):
    error_msg = ''
    if request.method =='POST':
        user = request.POST.get('username',None)
        if len(user)==0:
            error_msg='user name is null'
        else:
            return redirect('/home')
    return render(request,'login.html',{'msg':error_msg})