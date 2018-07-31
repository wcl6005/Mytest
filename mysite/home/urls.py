# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from . import home

urlpatterns = [
    url(r'^test/', home.test, name="test"), 
    url(r'^registerapi/', home.registerapi, name="registerapi"), 
    url(r'^loginapi/', home.loginapi, name="loginapi"), 

]