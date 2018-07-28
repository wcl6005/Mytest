# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from . import myhome

urlpatterns = [
    url(r'^test/', myhome.test, name="test"), 

]