# -*- coding: utf-8 -*-
from django.http.response import HttpResponseRedirect, HttpResponse

#  http://localhost:9000/apis/registerapi/ 
def registerapi(request):
    return HttpResponse('ok1')


#  http://localhost:9000/apis/loginapi/  
def loginapi(request):
    return HttpResponse('ok2')   
