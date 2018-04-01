# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate #django验证登录
from django.shortcuts import render
from django.http.response import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from myAPI.checkcode import gcheckcode

#注册 自己定义界面 验证码 前台验证  http://localhost:8000/register/
def register(request):
    g_checkcode = gcheckcode(request)#验证码送前台验证
    if request.method != 'POST':
        return  render(request, 'home/register.html' , context=locals())       
    username = request.POST['username']
    isname = User.objects.filter(username = username)
    if isname:  
        messages.info(request, username + '用户已经注册！')
        return HttpResponseRedirect('#')   
    password=request.POST['password']
    user = User.objects.create_user(username, username, password) 
    user.save()
    user = authenticate(username=request.POST['username'], password=password) 
    if user:        
        auth_login(request, user) #django登录
        return  HttpResponseRedirect('/index/')
    messages.info(request, username + '注册失败！')
    return HttpResponseRedirect('#')   
  
# 登录 自己定义界面 前台没有验证 http://localhost:8000/login/
def login(request):
    if request.method != 'POST':
        return  render(request, 'home/login.html', context=locals())
    user = authenticate(username=request.POST['username'], password=request.POST['password']) 
    if user:        
        auth_login(request, user) #django登录
        return  HttpResponseRedirect('/index/')
    messages.info(request, u'登录失败！请输入一个正确的 用户名和密码. 注意他们都是区分大小写的！')
    return  render(request, 'home/login.html', context=locals())

def index(request):
    return  render(request, 'index.html', context=locals())