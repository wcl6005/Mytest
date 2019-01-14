# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from . import home
urlpatterns = [    
    url(r'^$', home.img_recog, name="img_recog"),    
    url(r'^img_to_data/', home.img_to_data, name="img_to_data"),     
    url(r'^wx_uploadFile/', home.wx_uploadFile, name="wx_uploadFile"),     
]