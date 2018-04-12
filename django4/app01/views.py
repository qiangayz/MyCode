# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

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