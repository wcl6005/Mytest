# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^index/$', views.index, name="index"),
    url(r'^upload/$', views.upload, name="upload"),
    url(r'^upfolder/$', views.upfolder, name="upfolder"),
       
]
