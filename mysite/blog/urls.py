# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from django.urls import path
from . import views

urlpatterns = [
    path(r'index/', views.index, name="index"),
    path(r'upload/', views.upload, name="upload"),
    path(r'upfolder/', views.upfolder, name="upfolder"),
]
