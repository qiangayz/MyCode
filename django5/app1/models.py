# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Userinfo(models.Model):
    user = models.CharField(max_length=32)
    pwd = models.CharField(max_length=32)
    email = models.EmailField(max_length=32)