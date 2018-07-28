# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from myAPI import strAPI

@login_required
def index(request):
    s = strAPI.getstr()
    return  render(request, 'account/index.html', context=locals())

    