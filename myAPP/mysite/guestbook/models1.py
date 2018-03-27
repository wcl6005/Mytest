# -*- coding: utf-8 -*-
from __future__ import unicode_literals
#本框架 数据库名称不能用User，否则出错！
from django.contrib.auth.models import User
from django.db import models

#留言
class Guestbook(models.Model):
    username = models.ForeignKey(User, on_delete=models.PROTECT,blank=True, null=True)
    title = models.CharField(max_length=64,blank=True, null=True)
    tel = models.CharField(max_length=12,blank=True, null=True)
    content = models.TextField(max_length=256,blank=True, null=True)
    state = models.IntegerField(default=0) #单价 默认值0 回复的状态
    date = models.DateTimeField(auto_now=True, null=True, blank=True) #自动创建日期含时间
    def __unicode__(self):
        return self.title
#回复
class Reply(models.Model):
    username = models.ForeignKey(User, on_delete=models.PROTECT,blank=True, null=True)
    title = models.CharField(max_length=512,blank=True, null=True)
    content = models.TextField(max_length=256,blank=True, null=True)
    date = models.DateTimeField(auto_now=True, null=True, blank=True) #自动创建日期含时间
    def __unicode__(self):
        return self.title

    