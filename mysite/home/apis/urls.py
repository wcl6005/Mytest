# -*- coding: utf-8 -*-
from django.conf.urls import url, include
import users
#在 misite/misite/urls.py中，定义第一级路由名apis
#url(r'^apis/', include('apis.urls')),#定义第一级路由名apis

urlpatterns = [
    url(r'^registerapi/', users.registerapi, name="registerapi"),   
    url(r'^loginapi/', users.loginapi, name="loginapi"),            
]