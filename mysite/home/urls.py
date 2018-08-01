# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from . import home

# import os
# from django.shortcuts import render
# # try:
# #     import cStringIO as StringIO
# # except ImportError:
# #     import StringIO
# import random
# from django.http.response import HttpResponseRedirect, HttpResponse
#from PIL import Image, ImageDraw, ImageFont, ImageFilter

from myAPI import checkcode
urlpatterns = [
    url(r'^test/', home.test, name="test"), 
    url(r'^registerapi/', home.registerapi, name="registerapi"), 
    url(r'^loginapi/', home.loginapi, name="loginapi"), 
    url(r'^checkcodeGIF/', checkcode.checkcodeGIF, name="checkcodeGIF"),
    url(r'^getcheckcode/', checkcode.getcheckcode, name="getcheckcode"),


]