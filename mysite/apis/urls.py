# -*- coding: utf-8 -*-
from django.conf.urls import url, include
import users

urlpatterns = [
    url(r'^registerapi/', users.registerapi, name="registerapi"),   
    url(r'^loginapi/', users.loginapi, name="loginapi"),            
]