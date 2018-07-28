# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth import login as auth_login #当函数名是login，必须用auth_login
from django.contrib.auth import authenticate, login #django验证登录
from django.shortcuts import render
from django.http.response import HttpResponseRedirect, HttpResponse,\
    StreamingHttpResponse

from django.contrib import messages
from django.contrib.auth.models import User, Group

#  http://localhost:9000/home/index/
def index(request):
    return  HttpResponse('ok')
  
