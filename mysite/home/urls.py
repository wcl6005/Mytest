# -*- coding: utf-8 -*-
from django.conf.urls import url, include
import home


urlpatterns = [
    url(r'^test/', home.test, name="test"), # http://localhost:9000/home/index/           


]