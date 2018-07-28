# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth import login as auth_login 
from django.contrib.auth import authenticate, login 
from django.shortcuts import render
from django.http.response import HttpResponseRedirect, HttpResponse,\
    StreamingHttpResponse

from django.contrib import messages
from django.contrib.auth.models import User, Group

def test(request):    
    return  HttpResponse('ok')
  


