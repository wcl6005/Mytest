# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from . import myuser

urlpatterns = [
    url(r'^registerapi/', myuser.registerapi, name="registerapi"),   
    url(r'^loginapi/', myuser.loginapi, name="loginapi"),            
]