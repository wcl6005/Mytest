# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth import login as auth_login 
from django.contrib.auth import authenticate, login 
from django.shortcuts import render
from django.http.response import HttpResponseRedirect, HttpResponse,\
    StreamingHttpResponse

from django.contrib import messages
from django.contrib.auth.models import User, Group
from myAPI.checkcode import gcheckcode,create_validate_code

def myregister(request):
    path = 'home/myregister.html' 
    href = '/admin/auth/user/' 
    g_checkcode = gcheckcode(request)
    if request.method != 'POST':
        return  render(request, path, context=locals())       
    name = request.POST['username']
    isname = User.objects.filter(username = name)
    if isname: 
        messages.info(request, name + '用户已经注册！')
        return HttpResponseRedirect('#')   
    email = request.POST['email']
    password = request.POST['password']
    user = User.objects.create_user(name, email, password) 
    user.is_staff = False 
    user.is_superuser = False 
    user.save()
    return  HttpResponseRedirect(href)
  
def mylogin(request):
    if request.method != 'POST':
        return  render(request, 'home/mylogin.html', context=locals()) 
    username = request.POST['username']
    password = request.POST['password']
    filename = request.POST['filename']
    href = request.POST['href']
    if href == '':  href = '/home/index/' 
    user = authenticate(username=username, password=password) 
    if user: 
        auth_login(request, user)
        return  HttpResponseRedirect(href)
    messages.info(request, u'登录失败！请输入一个正确的 用户名 和密码. 注意他们都是区分大小写的！')
    return  render(request, 'home/mylogin.html', context=locals())
