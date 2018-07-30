# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from . import myusers

urlpatterns = [
    url(r'^registerapi/', myusers.registerapi, name="myregisterapi"),   
    url(r'^loginapi/', myusers.loginapi, name="myloginapi"),            
]