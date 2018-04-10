# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.shortcuts import redirect
from app01 import models
# Create your views here.
def business(request):
    # return HttpResponse('112312')
    v1=models.Business.objects.all()
    #QuerySet  上面语句会得到一个QuerySet 对象，对象有下面这些属性
    # [obj(id,caption,code),obj(id,caption,code),obj(id,caption,code) ]
    v2 = models.Business.objects.all().values('id', 'caption')
    #这个得到字典
    v3 = models.Business.objects.all().values_list('id', 'caption')
    #得到元组
    return render(request,'business.html',{'v1':v1,'v2':v2,'v3':v3})

def host(request):
    v1 = models.Host.objects.all()
    v2 = models.Host.objects.filter(nid__gt=0)
    print v1,'-----',v2,'----'
    for row in v2:
        print (row.nid,row.hostname,row.ip,row.port,row.b_id,row.b.caption,row.b.id)
    # return HttpResponse('112312')
    # v1 = models.Business.objects.filter(host__nid__gt=0)#也可以使用大于0的方式来获取
    return render(request, 'host.html', {'v1': v1})