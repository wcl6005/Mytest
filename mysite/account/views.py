# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http.response import HttpResponseRedirect, HttpResponse,\
    StreamingHttpResponse
from django.contrib.auth.decorators import login_required
from monthdelta import monthdelta
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


from django.contrib.auth.models import User, Group
import datetime
import os
import re
import tempfile
import uuid
import xlsxwriter

@login_required
def billing(request, page):  
    return render(request, 'account/billing.html', context=locals())

