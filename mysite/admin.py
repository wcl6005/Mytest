# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from mysite.guestbook.models import Guestbook,Reply

@admin.register(Guestbook)
class GuestbookAdmin(admin.ModelAdmin):    
    list_display = ('id','username','title','tel','content','state','date')
@admin.register(Reply)
class ReplyAdmin(admin.ModelAdmin):    
    list_display = ('id','username','guestbookname','title','content','date')
