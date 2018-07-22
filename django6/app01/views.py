# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
import json
from django.shortcuts import render, HttpResponse
from django import forms
from django.forms import fields as Ffields
from django.forms import widgets as Fwidegets
from app01 import models



# Create your views here.
class UserInfoModelForm(forms.ModelForm):
    is_rem = Ffields.CharField(
        widget=Fwidegets.CheckboxInput()
    )

    class Meta:
        model = models.UserInfo
        fields = '__all__'
        # fields = ['username','pwd']  选取
        # exclude = ['username']    排除
        labels = {
            'user': '用户名',
            'pwd': '密码',
            'email': '邮箱',
        }
        help_texts = {
            'user': '111111'
        }
        # widgets={
        #     'user':Fwidegets.Textarea(attrs={'style':'background-color:blue'})
        # }
        error_messages = {
            '__all__': {

            },
            'user': {'required': '用户名不能为空'}
        }
        # field_classes={
        #     'email':Ffields.URLField
        # }

    def clean_username(self):
        old = self.cleaned_data['user']
        print 'old is :', old
        return old


def index(request):
    if request.method == 'GET':
        obj = UserInfoModelForm()
        return render(request, 'index.html', {'obj': obj})

    if request.method == 'POST':
        obj = UserInfoModelForm(request.POST)
        if obj.is_valid():
            obj.save()
            # instance=obj.save(False)   等价于obj.save()
            # instance.save()
            # obj.save_m2m()

        # print obj.is_valid()
        # print obj.cleaned_data
        # print obj.errors

        # models.UserInfo.objects.create(**obj.cleaned_data)
        # models.UserInfo.objects.filter(id=1).update(**obj.cleaned_data)
        return render(request, 'index.html', {'obj': obj})


def user_list(request):
    li = models.UserInfo.objects.all().select_related('usertype')
    return render(request, 'user_list.html', {'li': li})


def user_edit(request, nid):
    # 获取当前的id的信息
    # 显示用户已经存在信息
    if request.method == "GET":
        user_obj = models.UserInfo.objects.filter(id=nid).first()
        mf = UserInfoModelForm(instance=user_obj)
        return render(request, 'user_edit.html', {'mf': mf, 'nid': nid})
    if request.method == "POST":
        user_obj = models.UserInfo.objects.filter(id=nid).first()
        mf = UserInfoModelForm(request.POST, instance=user_obj)
        if mf.is_valid():
            mf.save()
        else:
            print mf.errors
        return render(request, 'user_edit.html', {'mf': mf, 'nid': nid})


def ajax(request):
    print request.POST
    ret = {'code': True, 'data': None}
    return render(request, 'ajax.html', {'ret': ret})


def ajax_json(request):
    print request.POST
    ret = {'code': True, 'data': request.POST.get('username')}
    import json
    return HttpResponse(json.dumps(ret))

def upload(request):
    if request.method == "GET":
        return render(request,'upload.html')
    if request.method =="POST":
        pass

def upload_file(request):
    request.POST.get('username')
    fafafa = request.FILES.get('fileobj')
    img_path = os.path.join('static/img/',fafafa.name)
    with open( img_path, 'wb') as f:
        for item in fafafa.chunks():
            f.write(item)
    ret = {'code':True,'data':img_path}
    return HttpResponse(json.dumps(ret))
