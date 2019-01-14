# -*- coding: utf-8 -*-
#识别图像中的字符串 使用baidu-aip模块  优点是：快、准、简洁 
from django.shortcuts import render
from django.http.response import HttpResponseRedirect, HttpResponse
from django.http import JsonResponse   
from aip import AipOcr   # pip install  baidu-aip
import os
AppID = '11450107'
API_Key = 'uAA5KGXAzDDk2ewBa3dvRrWj'
Secret_Key = 'CgLyabrL4WH5KV0yyT074cMx8GyAnRGt'
IMG_NAME = 'img_name.jpg'
 
#  http://localhost:8000  
def img_recog(reuqest):  
    data = {'imgdata': '识别图像中的字符串 okokok!'}
    return JsonResponse(data) 

#  http://localhost:8000/img_to_data/  
def img_to_data(request):
    res = get_img_str(IMG_NAME)
    mylist = [{"res" : res}]
    print(res) 
    return JsonResponse(mylist, safe = False) 

#  http://localhost:8000/wx_uploadFile/ 
def wx_uploadFile(request):
    name = ''
    try:
        if request.FILES:
            MyImg = request.FILES.get("file", None)
            if MyImg:
                name = MyImg.name
                WriteFile(MyImg, IMG_NAME) #保存图像文件 IMG_NAME
    except Exception as ex:
        print(ex)
        name = ex 
    mylist = [{"name" : name}]
    return JsonResponse(mylist, safe = False) 

def get_img_str(name):
    s = ''
    client = AipOcr(AppID,API_Key,Secret_Key)
    img = open(name,'rb').read()
    msg = client.basicGeneral(img)
    for m in msg.get('words_result'):
        s += m.get('words') + '\n'
    return s


def WriteFile(fread,writefilepath):
    size = 1024 #每次读字节数
    fp = open(writefilepath,'w+') 
    while True:
        chunk = fread.read(size)
        if not chunk:
            break
        fp.write(chunk)       

   

