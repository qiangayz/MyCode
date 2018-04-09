# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class UserInfo(models.Model):
    username=models.CharField(max_length=32)
    password=models.CharField(max_length=64)

class zte(models.Model):
    id=models.AutoField(primary_key=True)  #主键，自增
    username=models.CharField(max_length=32)
    password=models.CharField(max_length=64)
    email=models.CharField(max_length=64,null=True)