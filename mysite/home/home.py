# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth import login as auth_login 
from django.contrib.auth import authenticate, login 
from django.shortcuts import render
from django.http.response import HttpResponseRedirect, HttpResponse

from django.contrib.auth.models import User, Group
from django.http import JsonResponse
from django.contrib import messages

import os
from django.shortcuts import render
try:
    import cStringIO as StringIO
except ImportError:
    import StringIO
from checkcode import create_validate_code,gcheckcode

#网页显示内存图片 http://localhost:9000/home/checkcodeGIF/
def checkcodeGIF(request):
    return  HttpResponse('ok')
#     if not request.session.get('checkcode',''):
#         request.session['checkcode'] = '1234'        
#     img_type="GIF" #图像类型
#     checkcode = create_validate_code(request)#获得图片+验证码
#     mstream = StringIO.StringIO()  #内存文件对象。read, readline, readlines, write, writelines都是有的mstream.write("aaaa")
#     checkcode[0].save(mstream, img_type) #图片保存在内存中
#     codeImg = mstream.getvalue() #获得保存图片
#     mstream.close()#关闭保存
#     return  HttpResponse(codeImg, img_type) #网页显示内存图片

# # http://localhost:9000/home/getcheckcode/
# def getcheckcode(request):
#     g_checkcode = gcheckcode(request)
#     path = request.GET.get('path','base.html')
#     return  render(request, path, context=locals())

#注册API  http://localhost:9000/home/registerapi/ 
def registerapi(request):
    if request.method != 'POST':
        mylist = list(User.objects.values())
        return  JsonResponse(mylist,safe=False)      
    name = request.POST['name']
    isname = User.objects.filter(username = name)
    if isname:  #判断name是否有相同的记录
        msgdict = {'msg': name + ' Username is already in name.'}
        return JsonResponse(msgdict)      
    password = request.POST['password']
    email = request.POST['email']
    user = User.objects.create_superuser(name, email, password)
    user.save() 
    return  JsonResponse({})

#登录API  http://localhost:9000/home/loginapi/  
def loginapi(request):   
    if request.method != 'POST':
        mylist = list(User.objects.values())
        return  JsonResponse(mylist,safe=False)      
    name = request.POST['name']
    password = request.POST['password']
    user = authenticate(username=name, password=password) #django验证登录
    if user:
        auth_login(request, user)#django登录
        return  JsonResponse({})      
    msgdict = {'msg':'user authenticate err!'}
    return JsonResponse(msgdict) 

def test(request):    
    return  HttpResponse('ok')
  


