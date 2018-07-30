# -*- coding: utf-8 -*-
#from django.contrib.auth.models import User, Group
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login 
from django.contrib.auth import login as auth_login 

 
def registerapi(request):
    if request.method != 'POST':
        mylist = [1,2]
        return  JsonResponse(mylist,safe=False)      

 
def loginapi(request):   
    if request.method != 'POST':
        mylist = [1,2]
        return  JsonResponse(mylist,safe=False)      
