# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from . import home
# from myAPI import checkcode
urlpatterns = [
    url(r'^test/', home.test, name="test"), 
    url(r'^registerapi/', home.registerapi, name="registerapi"), 
    url(r'^loginapi/', home.loginapi, name="loginapi"), 

#     url(r'^checkcodeGIF/', checkcode.checkcodeGIF, name="checkcodeGIF"), # 
#     url(r'^getcheckcode/', checkcode.getcheckcode, name="getcheckcode"), #        

]