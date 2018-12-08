# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from django.urls import path
from . import views

urlpatterns = [
    path(r'index0/', views.index0, name="index0"),
    
    path(r'index1/', views.index1, name="index1"),
    path(r'index2/', views.index2, name="index2"),
    
    path(r'index3/', views.index3, name="index3"),
    

]
