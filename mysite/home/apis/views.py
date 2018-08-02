# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http.response import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.http import JsonResponse


# http://localhost:9000/apis/registerapi/ 
def registerapi(request):
    if request.method != 'POST':
        mylist = list(User.objects.values())
        return  JsonResponse(mylist,safe=False)      
    name = request.POST['name']
    isname = User.objects.filter(username = name)
    if isname:  
        msgdict = {'msg': name + ' Username is already in name.'}
        return JsonResponse(msgdict)      
    password = request.POST['password']
    email = request.POST['email']
    user = User.objects.create_superuser(name, email, password)
    user.save() 
    return  JsonResponse({})

#  http://localhost:9000/api/loginapi/  
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