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

# def host(request):
#     v1 = models.Host.objects.all()
#     # v2 = models.Host.objects.filter(nid__gt=0)
#     # print v1,'-----',v2,'----'
#     # for row in v2:
#     #     print (row.nid,row.hostname,row.ip,row.port,row.b_id,row.b.caption,row.b.id)
#     # return HttpResponse('112312')
#     # v1 = models.Business.objects.filter(host__nid__gt=0)#也可以使用大于0的方式来获取
#     #使用value获取到一个字典，然后使用b__caption双下划线直接获取到外键属性的值
#     v2 = models.Host.objects.filter(nid__gt=0) .values('nid','hostname','b_id','b__caption')
#     # print v2
#     #使用value_list获取到一个元组
#     v3 = models.Host.objects.filter(nid__gt=0) .values_list('nid','hostname','b_id','b__caption')
#     print v3
#
#     return render(request, 'host.html', {'v1': v1,'v2':v2,'v3':v3})

def host(request):
    if request.method=="GET":
        v1 = models.Host.objects.all()
        v2 = models.Host.objects.filter(nid__gt=0) .values('nid','hostname','b_id','b__caption')
        v3 = models.Host.objects.filter(nid__gt=0) .values_list('nid','hostname','b_id','b__caption')
        b_list=models.Business.objects.all()

        return render(request, 'host.html', {'v1': v1,'v2':v2,'v3':v3,'b_list':b_list})
    elif request.method=="POST":
        h=request.POST.get('hostname')
        i=request.POST.get('ip')
        p=request.POST.get('port')
        b=request.POST.get('b_id')
        models.Host.objects.create(hostname=h,ip=i,port=p,b_id=b)
        return redirect('/host')

# def test_ajax(request):
#     h = request.POST.get('hostname')
#     i = request.POST.get('ip')
#     p = request.POST.get('port')
#     b = request.POST.get('b_id')
#
#     if h and len(h)>5:
#         models.Host.objects.create(hostname=h,
#                                    ip=i,
#                                    port=p,
#                                    b_id=b)
#         return HttpResponse('OK')
#     else:
#         return HttpResponse('太短了')
def test_ajax(request):
    import json
    ret={'status':True,'error':None,'data':None}
    try:
         h = request.POST.get('hostname')
         i = request.POST.get('ip')
         p = request.POST.get('port')
         b = request.POST.get('b_id')

         if h and len(h)>5:
             models.Host.objects.create(hostname=h,
                                        ip=i,
                                        port=p,
                                        b_id=b)
             return HttpResponse('OK')
         else:
             ret['status'] = False
             ret['error'] = '太短了'
    except Exception as e:
        ret['status'] = False
        ret['error']='请求错误'
    return HttpResponse(json.dumps(ret))

def app(request):
    return render(request,'app.html')