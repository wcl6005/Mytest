# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http.response import HttpResponseRedirect, HttpResponse

from myAPI import strAPI

#  http://localhost:9000/apis/index/ 
def index(request):
    s = strAPI.getstr()
    return  HttpResponse(s)

    