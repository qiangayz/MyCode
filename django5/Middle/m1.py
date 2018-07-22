# -*- coding: utf-8 -*-
from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse

class Row1(MiddlewareMixin):
    def process_request(self,request):
        print ('第一步')

    def process_view(self, request, view_func, view_func_args, view_func_kwargs):
        print('中间第一步')

    def process_response(self,request,response):
        print ('倒数第一步')
        return  response

class Row2(MiddlewareMixin):
    def process_request(self,request):
        print ('第2步')

    def process_view(self, request, view_func, view_func_args, view_func_kwargs):
        print('中间第2步')

    def process_response(self,request,response):
        print ('倒数第2步')
        return  response

class Row3(MiddlewareMixin):
    def process_request(self,request):
        print ('第3步')

    def process_view(self, request, view_func, view_func_args, view_func_kwargs):
        print('中间第3步')

    def process_response(self,request,response):
        print ('倒数第3步')
        return  response

    def process_exception(self, request, exception):
        if isinstance(exception,ValueError):
            return HttpResponse('出现异常》。。')

    def process_template_response(self,request,response):
        # 如果Views中的函数返回的对象中，具有render方法
        print('-----------------------')
        return response
