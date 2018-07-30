# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from . import views
# 本级路由：/account/
urlpatterns = [
    url(r'^index/$', views.index, name="index"),  # /account/index/
    
]
