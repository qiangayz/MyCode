# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Host(models.Model):
    nid = models.AutoField(primary_key=True)  # 主键一般自动生成，也可以自己设定，但是需要声明primary_key
    hostname = models.CharField(max_length=32, db_index=True)  # db_index添加索引
    ip = models.GenericIPAddressField(protocol="ipv4", db_index=True)  # db_index添加索引设置字段为ip模式
    port = models.IntegerField()
    b = models.ForeignKey(to="Business", to_field='id')

class Business(models.Model):
    caption = models.CharField(max_length=32)
    code = models.CharField(max_length=32, null=True, default="SA")
    # fk = models.ForeignKey('Foo')

class Application(models.Model):
    name = models.CharField(max_length=32)
    r = models.ManyToManyField("Host")
# 2
class HostToApp(models.Model):
    hobj = models.ForeignKey(to='Host',to_field='nid')
    aobj = models.ForeignKey(to='Application',to_field='id')

# hid: 1~10  aid:1~2