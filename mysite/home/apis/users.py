# -*- coding: utf-8 -*-

from django.contrib.auth.models import User, Group
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login 
from django.contrib.auth import login as auth_login 


# def registerapi(request):
#     if request.method != 'POST':
#         mylist = list(User.objects.values())
#         return  JsonResponse(mylist,safe=False)      
#     name = request.POST['name']
#     isname = User.objects.filter(username = name)
#     if isname: 
#         msgdict = {'msg': name + ' Username is already in name.'}
#         return JsonResponse(msgdict)      
#     password = request.POST['password']
#     email = request.POST['email']
#     user = User.objects.create_superuser(name, email, password)
#     user.save() 
#     return  JsonResponse({})
# 
# 
# def loginapi(request):   
#     if request.method != 'POST':
#         mylist = list(User.objects.values())
#         return  JsonResponse(mylist,safe=False)      
#     name = request.POST['name']
#     password = request.POST['password']
#     user = authenticate(username=name, password=password) 
#     if user:
#         auth_login(request, user)
#         return  JsonResponse({})      
#     msgdict = {'msg':'user authenticate err!'}
#     return JsonResponse(msgdict) 