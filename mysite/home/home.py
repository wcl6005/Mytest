# -*- coding: utf-8 -*-
from django.contrib.auth import login as auth_login 
from django.contrib.auth import authenticate, login 
from django.shortcuts import render
from django.http.response import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from myAPI.checkcode import gcheckcode
from myAPI import strAPI
def index(request):
    s = strAPI.getstr()
    return  render(request, 'home/index.html', context=locals())

#  http://localhost:9000/home/myregister/
def myregister(request):
    path = 'home/myregister.html' #html路径
    href = '/admin/auth/user/' #注册成功，重新定向
    g_checkcode = gcheckcode(request)#验证码送前台验证
    if request.method != 'POST':
        return  render(request, path, context=locals())       
    name = request.POST['username']
    isname = User.objects.filter(username = name)
    if isname:  #判断name是否有相同的记录
        messages.info(request, name + '用户已经注册！')
        return HttpResponseRedirect('#')   
    email = request.POST['email']
    password = request.POST['password']
    user = User.objects.create_user(name, email, password) #用户,不能从Django自带登录界面，登录
    user.is_staff = False #非职员 默认False
    user.is_superuser = False #非超级用户 默认False
    user.save()
    return  HttpResponseRedirect(href)
  
# http://localhost:9000/home/mylogin/
def mylogin(request):
    if request.method != 'POST':
        return  render(request, 'home/mylogin.html', context=locals()) 
    username = request.POST['username']
    password = request.POST['password']
    filename = request.POST['filename']
    href = request.POST['href']
    if href == '':  href = '/home/index/' #href空，转index
    user = authenticate(username=username, password=password) #django验证登录
    if user: 
        auth_login(request, user)#当函数名是login，必须用auth_login
        #login(request, user)#函数名不能用login ！！！
        return  HttpResponseRedirect(href)
    messages.info(request, u'登录失败！请输入一个正确的 用户名 和密码. 注意他们都是区分大小写的！')
    return  render(request, 'home/mylogin.html', context=locals())



