# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from . import home
urlpatterns = [    
    url(r'^$', home.index, name="index"),
    url(r'^tostr/', home.tostr, name="tostr"),     
    url(r'^recog_img/', home.recog_img, name="recog_img"),    
  
    url(r'^apidict/', home.apidict, name="apidict"),  
    url(r'^apidata/', home.apidata, name="apidata"),     
    url(r'^distinguish_img/', home.distinguish_img, name="distinguish_img"),     
    url(r'^wx_uploadFile/', home.wx_uploadFile, name="wx_uploadFile"),     

]