# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from . import home

urlpatterns = [
    url(r'^test/', home.test, name="test"), 

]