# -*- coding: utf-8 -*-
from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^billing/(?P<page>\d*)?$', views.billing, name='billing'),

]
