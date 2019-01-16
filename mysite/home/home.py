# -*- coding: utf-8 -*-
#识别图像中的字符串 使用baidu-aip模块  优点是：快、准、简洁 
# 微信小程序在开发工具上执行POST请求这里(服务器)可以接受到数据；但是手机预览时执行POST请求这里(服务器)接受不到数据
# 原因：域名信息未设置 https://blog.csdn.net/ycocol/article/details/79295504

from django.shortcuts import render
from django.http.response import HttpResponseRedirect, HttpResponse
from django.http import JsonResponse   
from aip import AipOcr   # pip install  baidu-aip
import os
from django.views.decorators.csrf import csrf_exempt
AppID = '11450107'
API_Key = 'uAA5KGXAzDDk2ewBa3dvRrWj'
Secret_Key = 'CgLyabrL4WH5KV0yyT074cMx8GyAnRGt'
IMG_NAME = 'test_img.jpeg'

#  http://localhost:8000  
def recog_img(reuqest):         
    res = get_distinguish_img_str(IMG_NAME)
    mylist = [{"res" : res}] 
    return JsonResponse(mylist, safe = False) 

def apidata(request):
    res = 'hello world !'
    if request.method == 'POST':
        res += request.POST['res']
    mylist = [{"res" : res}] 
    return JsonResponse(mylist, safe = False) 

#  http://localhost:8000/distinguish_img/  
def distinguish_img(request):
    name ='name_img.jpg'   
    res = get_distinguish_img_str(name)
    mylist = [{"res" : res}] 
    return JsonResponse(mylist, safe = False) 

headers = {"Content-Type": "application/x-www-form-urlencoded"} 

#  http://localhost:8000/wx_uploadFile/  
@csrf_exempt
def wx_uploadFile(request):
    with open('aa_bb.jpg','wb') as file:
        file.write("ok".encode("utf-8"))
    name = 'None' 
    if request.method == 'POST':   
        myfile = request.FILES.get("file", None)                              
        if myfile:
            WriteFile(myfile)
            name = myfile.name 
        else:    
            if os.path.exists('name_img.jpg'):
                os.remove('name_img.jpg')        
    mylist = [{"name" : name}] 
    return JsonResponse(mylist, safe = False) 


# def wx_uploadFile(request):
#     name = ''    
#     myfile = request().FILES.get("file", None)
#     if myfile:
#         WriteFile(myfile) 
#     else:
#         with open('name_img.jpg','wb') as file:
#             file.write('err'.encode("utf-8"))                           
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
            file.write(str(ex).encode("utf-8"))

   

