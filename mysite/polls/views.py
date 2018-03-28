# -*- coding: utf-8 -*-
from django.shortcuts import render
from .models import Poem

# Create your views here.
#电影模板 http://localhost:8000/film/index.html/
def film(request,s):
    return render(request, 'templatefree/film/'+s, context=locals())