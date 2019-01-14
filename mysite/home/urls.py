# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from . import home
urlpatterns = [    
    url(r'^$', home.img_recog, name="img_recog"),    
    url(r'^distinguish_img/', home.distinguish_img, name="distinguish_img"),     
    url(r'^wx_uploadFile/', home.wx_uploadFile, name="wx_uploadFile"),     
]