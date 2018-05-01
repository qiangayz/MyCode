#coding=utf-8
"""django2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from app01 import views

urlpatterns = [
     url(r'^admin/', admin.site.urls),
      url(r'^index/', views.index),
      url(r'^userinfo/', views.userinfo),
      url(r'^userdetail-(?P<nid>\d+)/', views.userdetail),
      url(r'^userdel-(?P<nid>\d+)/', views.userdel),
      url(r'^useredit-(?P<nid>\d+)/', views.user_edit),
      url(r'^orm/', views.orm),
     url(r'^indexssssssssssssssssss/(\d+)/', views.index,name='indexx'),
     url(r'^login/', views.login),
#     url(r'^home/', views.Home.as_view()),
     url(r'^detail/', views.detail),
     url(r'^detail-(\d+).html', views.detail2),
#     url(r'^detail-(?P<nid>\d+)-(?P<uid>\d+).html', views.detail3),
#     url(r'^detail-(?P<nid>\d+)-(?P<uid>\d+).html', views.detail3),
#
 ]

