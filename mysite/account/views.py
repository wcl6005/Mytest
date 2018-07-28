# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http.response import HttpResponseRedirect, HttpResponse,\
    StreamingHttpResponse
from django.contrib.auth.decorators import login_required
from monthdelta import monthdelta
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Company, Material, Order
from django.contrib.auth.models import User, Group
import datetime
import os
import re
import tempfile
import uuid
import xlsxwriter
from myAPI import strAPI


def index(request):
    s = strAPI.getstr()
    return  render(request, 'account/index.html', context=locals())

    