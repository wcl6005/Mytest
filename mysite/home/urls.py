# -*- coding: utf-8 -*-
from django.conf.urls import url, include

from django.views.generic import TemplateView, ListView, View


class IndexView(TemplateView):
    template_name = 'home/index.html'

urlpatterns = [
    url(r'^index/$', IndexView.as_view()), 

]