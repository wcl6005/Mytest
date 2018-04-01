# -*- coding: utf-8 -*-
"""myAPP URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url,include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView, ListView, View
class IndexView(TemplateView):
    template_name = 'home.html'

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
    
    url(r'^', include('mysite.home.urls')),#定义第一级路由名home  
    url(r'^guestbook/', include('mysite.guestbook.urls')),

    url(r'^$', IndexView.as_view()),
    url(r'^index/$', IndexView.as_view(template_name='index.html')),
    url(r'^contact/$', IndexView.as_view(template_name='contact.html')),
    url(r'^about/$', IndexView.as_view(template_name='about.html')),
    url(r'^website/$', IndexView.as_view(template_name='website.html')),  
    url(r'^Trusteeship/$', IndexView.as_view(template_name='Trusteeship.html')),

    url(r'^wx/$', IndexView.as_view(template_name='wx/index.html')),

    #留言板
    url(r'^liuyan/$', IndexView.as_view(template_name='guestbook/liuyan.html')),
    #编辑器
    url(r'^editor/$', IndexView.as_view(template_name='guestbook/editor.html')),  
]
