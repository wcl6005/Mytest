# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http.response import HttpResponseRedirect, HttpResponse
from django.http import JsonResponse   
from aip import AipOcr   # pip install  baidu-aip
import os
AppID = '11450107'
API_Key = 'uAA5KGXAzDDk2ewBa3dvRrWj'
Secret_Key = 'CgLyabrL4WH5KV0yyT074cMx8GyAnRGt'

#使用baidu-aip模块 识别图像中的中文okokok! 优点是：快、准、简洁 
#  http://localhost:8000/home/img_recognitions  
def img_recog(reuqest):  
    data = {'imgdata': 'ok'}
    return JsonResponse(data) 

IMG_NAME = 'img_name.jpg'
#  http://localhost:8000/distinguish_img/  
def distinguish_img(request):
    res = ''
    client = AipOcr(AppID,API_Key,Secret_Key)
    img = open(IMG_NAME,'rb').read()
    msg = client.basicGeneral(img)
    for m in msg.get('words_result'):
        res += m.get('words') + '\n '
    mylist = [{"res" : res}]
    print(res) 
    return JsonResponse(mylist, safe = False) 

#  http://localhost:8000/wx_uploadFile/ 
def wx_uploadFile(request):
    name = ''
    if request.FILES:
        MyImg = request.FILES.get("file", None)
        if MyImg:
            name = MyImg.name
            if not WriteFile(MyImg,IMG_NAME): #保存图像文件 name_img.jpg
                name = ''
    mylist = [{"name" : name}] 
    return JsonResponse(mylist, safe = False) 

def WriteFile(fread,writefilepath):
    size = 1024 #每次读字节数
    fp = open(writefilepath,'w+') #打开文件
    try:
        while True:
            chunk = fread.read(size)
            if not chunk:
                break
            fp.write(chunk)
        fp.close()
    except Exception as ex:
        print(ex)
        return False
    return True
   

