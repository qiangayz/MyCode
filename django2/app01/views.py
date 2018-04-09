# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.shortcuts import redirect

# Create your views here.
# USER_DICT={
#     "k1":"root1",
#     "k2":"root2",
#     "k3":"root3",
#     "k4":"root4",
# }
USER_DICT={
    "1":{"name":"root1","email":"123"},
    "2":{"name":"root2","email":"123"},
    "3":{"name":"root3","email":"123"},
    "4":{"name":"root4","email":"123"},
}
def index(request):
    return  render(request,"index.html",{'user_dict':USER_DICT})

def userinfo(request):
    if request.method =="GET":
        user_list=models.UserInfo.objects.all()
        return render(request,'userinfo.html',{'user_list':user_list})
    elif request.method == "POST":
        u = request.POST.get('user')
        p = request.POST.get('pwd')
        models.UserInfo.objects.create(username=u,password=p)
        return redirect('/CC/userinfo/')

def userdetail(request,nid):
    obj=models.UserInfo.objects.filter(id=nid).first()
    return render(request,'userdetail.html',{'obj':obj})

def userdel(request,nid):
    models.UserInfo.objects.filter(id=nid).delete()
    return redirect('/CC/userinfo/')

def user_edit(request, nid):
    if request.method == "GET":
        obj = models.UserInfo.objects.filter(id=nid).first()
        return render(request, 'user_edit.html',{'obj': obj})
    elif request.method == "POST":
        nid = request.POST.get('id')
        u = request.POST.get('username')
        p = request.POST.get('password')
        models.UserInfo.objects.filter(id=nid).update(username=u,password=p)
        return redirect('/CC/userinfo/')

def detail(request):
    print '2222222222222',request.GET
    nid =request.GET.get("nid")
    detail_info = USER_DICT[nid]
    return render(request,'detail.html',{"dict":detail_info})

def detail2(request,nid):
    print '2222222222222',request.GET
    # nid =request.GET.get(nid)
    detail_info = USER_DICT[nid]
    return render(request,'detail.html',{"dict":detail_info})

def detail3(request,**kwargs):
    print kwargs

# def login(request):
#     data=[]
#     print "2222222222222222222",request.method
#     if request.method == "GET":
#         return render(request,"login.html")
#     elif request.method == "POST":
#         u = request.POST.get('username')
#         p = request.POST.get('password')
#         data.append(u)
#         data.append(p)
#         #radio
#         radio=request.POST.get('gender')
#         print radio
#         data.append(radio)
#         favor=request.POST.getlist('favor')
#         print favor
#         data.append(favor)
#         city = request.POST.get('city')
#         print city
#         data.append(city)
#         city1 = request.POST.getlist('city1')
#         print city1
#         data.append(city1)
#         obj=request.FILES.get('fafafa')
#         print obj,type(obj),obj.name
#         data.append(obj.name)
#         import os
#         file_path=os.path.join('upload',obj.name)
#         f= open(file_path,mode="wb")
#         for i in obj.chunks():
#             f.write(i)
#         f.close()
#         # if u == "zq" and p =="qwe":
#         #     return redirect("/index/")
#         # else:
#         return render(request,"login.html",{"msg":data})
#     else:
#         return redirect("/index/")
def login(request):
    print "2222222222222222222",request.method
    if request.method == "GET":
        return render(request,"login.html")
    elif request.method == "POST":
        u = request.POST.get('username')
        p = request.POST.get('password')
        obj=models.UserInfo.objects.filter(username=u,password=p).first()
        count=models.UserInfo.objects.filter(username=u,password=p).count()
        if obj:
            return redirect("/CC/index/")
        else:
            return render(request, "login.html")
from django.views import View
class Home(View):

    def dispatch(self,request,*args,**kwargs):
        print 'before'
        result=super(Home,self).dispatch(request,*args,**kwargs)
        print 'after'
        return  result

    def get(self,request):
        print request.method
        return render(request,"home.html")

    def post(self,request):
        print request.method
        return render(request, "home.html")

from app01 import models
def orm(request):
    #增加数据
    # models.UserInfo.objects.create(username='root',password='root123')
    # obj = models.UserInfo(username='zte',password='zte')
    # obj.save()
    # dict1={'username':'zte1',"password":'zte1' }
    # obj = models.UserInfo(**dict1)
    # obj.save()
    #查找数据
    # result=models.UserInfo.objects.all()
    # # print result
    # for row in result:
    #     print row.id,row.username,row.password
    # result = models.UserInfo.objects.filter(username='root')
    # result = models.UserInfo.objects.filter(username='root',password='root123')
    # for row in result:
    #     print row.id,row.username,row.password
    #删除
    # models.UserInfo.objects.filter(id='4').delete()
    #更新
    models.UserInfo.objects.all().update(password=123)
    return HttpResponse('adasd')