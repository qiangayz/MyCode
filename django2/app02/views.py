# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import redirect

# Create your views here.
def login(request):
    data=[]
    print "2222222222222222222",request.method
    if request.method == "GET":
        return render(request,"login.html")
    elif request.method == "POST":
        u = request.POST.get('username')
        p = request.POST.get('password')
        data.append(u)
        data.append(p)
        #radio
        radio=request.POST.get('gender')
        print radio
        data.append(radio)
        favor=request.POST.getlist('favor')
        print favor
        data.append(favor)
        city = request.POST.get('city')
        print city
        data.append(city)
        city1 = request.POST.getlist('city1')
        print city1
        data.append(city1)
        obj=request.FILES.get('fafafa')
        print obj,type(obj),obj.name
        data.append(obj.name)
        import os
        file_path=os.path.join('upload',obj.name)
        f= open(file_path,mode="wb")
        for i in obj.chunks():
            f.write(i)
        f.close()
        # if u == "zq" and p =="qwe":
        #     return redirect("/index/")
        # else:
        return render(request,"login.html",{"msg":data})
    else:
        return redirect("/index/")