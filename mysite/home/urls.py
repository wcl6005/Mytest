# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from . import home
urlpatterns = [    
    url(r'^$', home.recog_img, name="recog_img"),    
    url(r'^apidata', home.apidata, name="apidata"),     
    url(r'^distinguish_img/', home.distinguish_img, name="distinguish_img"),     
    url(r'^wx_uploadFile/', home.wx_uploadFile, name="wx_uploadFile"),     

]