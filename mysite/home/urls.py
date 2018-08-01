# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from . import home

from django.views.generic import TemplateView, ListView, View
from myAPI import checkcode

 
# 本级路由：/home/
class IndexView(TemplateView):
    template_name = 'home/index.html'

urlpatterns = [
    url(r'^test/', home.test, name="test"), 
    url(r'^registerapi/', home.registerapi, name="registerapi"), 
    url(r'^loginapi/', home.loginapi, name="loginapi"), 
    url(r'^checkcodeGIF/', checkcode.checkcodeGIF, name="checkcodeGIF"), # 
    url(r'^getcheckcode/', checkcode.getcheckcode, name="getcheckcode"), #        

]