# -*- coding: utf-8 -*-
from django.conf.urls import url, include
import home
from django.views.generic import TemplateView, ListView, View


#http://localhost:9000/home/index/    
urlpatterns = [
    url(r'^index/', home.index, name="index"),         
]