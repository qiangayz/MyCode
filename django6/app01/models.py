# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class UserType(models.Model):
    caption=models.CharField(max_length=32)

    def __unicode__(self):
        return self.caption

class UserGroup(models.Model):
    name=models.CharField(max_length=32)

    def __unicode__(self):
        return self.name

class UserInfo(models.Model):
    user = models.CharField(max_length=32)
    pwd = models.CharField(max_length=32)
    email = models.EmailField(max_length=32)
    usertype=models.ForeignKey(to='UserType',to_field='id')
    u2g=models.ManyToManyField(UserGroup)

