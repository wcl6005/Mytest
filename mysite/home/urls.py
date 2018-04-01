# -*- coding: utf-8 -*-
from django.conf.urls import url, include
import home
from myAPI import checkcode
from django.views.generic import TemplateView, ListView, View

# class IndexView(TemplateView):
#     template_name = 'home/__base__.html'
    
#http://localhost:8000/checkcodeGIF/
urlpatterns = [   
    url(r'^checkcodeGIF/', checkcode.checkcodeGIF, name="checkcodeGIF"), # 
    url(r'^getcheckcode/', checkcode.getcheckcode, name="getcheckcode"), # 
      
    url(r'^register/', home.register, name="register"), #   
    url(r'^login/', home.login, name="login"),
    url(r'^index/', home.index, name="index"),
 

]