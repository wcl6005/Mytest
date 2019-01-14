# -*- coding: utf-8 -*-
#识别图像中的字符串 使用baidu-aip模块  优点是：快、准、简洁 
from django.shortcuts import render
from django.http.response import HttpResponseRedirect, HttpResponse
from django.http import JsonResponse   
from aip import AipOcr   # pip install  baidu-aip
import os
from setuptools.command.build_ext import if_dl
AppID = '11450107'
API_Key = 'uAA5KGXAzDDk2ewBa3dvRrWj'
Secret_Key = 'CgLyabrL4WH5KV0yyT074cMx8GyAnRGt'
IMG_NAME = 'img_name.jpg'
 
#  http://localhost:8000  
def img_recog(reuqest):  
    data = {'imgdata': '识别图像中的字符串 okokok!'}
    return JsonResponse(data) 

#  http://localhost:8000/distinguish_img/  
def distinguish_img(request):
    name ='name_img.jpg'   
    res = get_distinguish_img_str(name)
    mylist = [{"res" : res}] 
    return JsonResponse(mylist, safe = False) 

#  http://localhost:8000/wx_uploadFile/  
def wx_uploadFile(request):
    if request.method == 'POST':   
        myfile = request.FILES.get("file", None)                              
        if myfile:
            WriteFile(myfile)  
        else:    
            if os.path.exists('name_img.jpg'):
                os.remove('name_img.jpg')
                myfile = None         
    mylist = [{"name" : myfile}] 
    return JsonResponse(mylist, safe = False) 


# def wx_uploadFile(request):
#     name = ''
#     if request.method == 'POST':   
#         myfile = request.FILES.get("file", None)
#         if myfile:
#             WriteFile(myfile) 
#         else:
#             with open('name_img.jpg','wb') as file:
#                 file.write('err')
#                          
#     mylist = [{"name" : name}] 
#     return JsonResponse(mylist, safe = False) 

def get_distinguish_img_str(name):
    s = ''
    try:
        client = AipOcr(AppID,API_Key,Secret_Key)
        img = open(name,'rb').read()
        msg = client.basicGeneral(img)
        for m in msg.get('words_result'):
            s += m.get('words') + '\n'
    except Exception as ex:
        s = str(ex)
    if not s:
        s = 'No Img Data !'
    return s
 
def WriteFile(myfile):
    try:
        with open('name_img.jpg','wb') as file:
            file.write(myfile.read())
    except Exception as ex:
        with open('name_img.jpg','wb') as file:
            file.write(str(ex))

   

