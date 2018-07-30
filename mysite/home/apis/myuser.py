# -*- coding: utf-8 -*-
from django.http.response import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User, Group
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login #django验证登录
from django.contrib.auth import login as auth_login #当函数名是login，必须用auth_login

#注册API  http://localhost:9000/apis/registerapi/ 
def registerapi(request):
    return HttpResponse('ok')
#     if request.method != 'POST':
#         mylist = list(User.objects.values())
#         return  JsonResponse(mylist,safe=False)      
#     name = request.POST['name']
#     isname = User.objects.filter(username = name)
#     if isname:  #判断name是否有相同的记录
#         msgdict = {'msg': name + ' Username is already in name.'}
#         return JsonResponse(msgdict)      
#     password = request.POST['password']
#     email = request.POST['email']
#     user = User.objects.create_superuser(name, email, password)
#     user.save() 
#     return  JsonResponse({})

#登录API  http://localhost:9000/apis/loginapi/  
def loginapi(request):
    return HttpResponse('ok')   
#     if request.method != 'POST':
#         mylist = list(User.objects.values())
#         return  JsonResponse(mylist,safe=False)      
#     name = request.POST['name']
#     password = request.POST['password']
#     user = authenticate(username=name, password=password) #django验证登录
#     if user:
#         auth_login(request, user)#django登录
#         return  JsonResponse({})      
#     msgdict = {'msg':'user authenticate err!'}
#     return JsonResponse(msgdict) 