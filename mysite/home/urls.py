# -*- coding: utf-8 -*-
from django.conf.urls import url, include
#import home
from django.views.generic import TemplateView, ListView, View
#from myAPI import checkcode

class IndexView(TemplateView):
    template_name = 'home/index.html'

urlpatterns = [
    url(r'^index/$', IndexView.as_view()), 
#     url(r'^checkcodeGIF/', checkcode.checkcodeGIF, name="checkcodeGIF"), 
#     url(r'^getcheckcode/', checkcode.getcheckcode, name="getcheckcode"),        
#     url(r'^myregister/', home.myregister, name="myregister"),    
#     url(r'^mylogin/', home.mylogin, name="mylogin"),

]