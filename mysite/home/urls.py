# -*- coding: utf-8 -*-
from django.conf.urls import url, include
import home
from django.views.generic import TemplateView, ListView, View
from myAPI import checkcode

#home应用，settings.py/INSTALLED_APPS   添加'home.apps.AccountConfig', 
# 本级路由：/home/
class IndexView(TemplateView):
    template_name = 'home/index.html'

urlpatterns = [
    url(r'^index/$', IndexView.as_view()), #url(r'^index/', home.index, name="index"), #优化掉视图了 http://localhost:9000/home/index/           
    url(r'^checkcodeGIF/', checkcode.checkcodeGIF, name="checkcodeGIF"), # 
    url(r'^getcheckcode/', checkcode.getcheckcode, name="getcheckcode"), #        
    url(r'^myregister/', home.myregister, name="myregister"), #   
    url(r'^mylogin/', home.mylogin, name="mylogin"),
    
#     url(r'^vuesignin/$', IndexView.as_view(template_name='home/signin.html')), ##url(r'^vuesignin/', home.vuesignin, name="vuesignin"),#优化掉视图了 http://localhost:9000/home/vuesignin/     
#     url(r'^vueregister/', home.vueregister, name="vueregister"),   

#     url(r'^modLoginRunoob/', home.modLoginRunoob, name="modLoginRunoob"),       

]