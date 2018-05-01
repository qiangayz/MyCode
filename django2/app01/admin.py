# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from app01.models import UserInfo
from app01.models import Zte
# Register your models here.

class UserInfoAdmin(admin.ModelAdmin):
    pass

class zte(admin.ModelAdmin):
    pass

admin.site.register(UserInfo,UserInfoAdmin)
admin.site.register(Zte,zte)