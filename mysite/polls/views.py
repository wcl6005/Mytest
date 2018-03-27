# -*- coding: utf-8 -*-
from django.shortcuts import render
from .models import Poem
from django.http.response import HttpResponseRedirect, HttpResponse

# Create your views here.
def home(request):
    #poems = Poem.objects.all()
    return render(request, 'base.html', context=locals())

#电影模板 http://localhost:8000/film/
def film(request):  
    return render(request, 'templatefree/film/main.html', context=locals())

def index(request,s):
    return render(request, 'polls/'+s+'.html', context=locals())