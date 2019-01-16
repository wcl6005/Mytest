# -*- coding: utf-8 -*-
#识别图像中的字符串 使用baidu-aip模块  优点是：快、准、简洁 
# 微信小程序在开发工具上执行POST请求这里(服务器)可以接受到数据；但是手机预览时执行POST请求这里(服务器)接受不到数据
# 原因：域名信息未设置 https://blog.csdn.net/ycocol/article/details/79295504
#headers = {"Content-Type": "application/x-www-form-urlencoded"}

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
def index(request):
    return  render(request, 'index.html', context=locals())    

#  http://localhost:8000  
def recog_img(request):         
    res = get_distinguish_img_str(IMG_NAME)
    mylist = [{"res" : res}] 
    return JsonResponse(mylist, safe = False) 

def apidict(request):
    mydict ={"result":[{"catid":"1","upid":"0","catname":"PhoneGap\u5e73\u53f0\u8d44\u8baf","subcate":[]},{"catid":"8","upid":"0","catname":"\u89c6\u9891\u6559\u7a0b","subcate":[{"catid":"9","upid":"8","catname":"PhoneGap \u89c6\u5c4f\u6559\u7a0b"},{"catid":"10","upid":"8","catname":"Sencha Touch \u6559\u7a0b"},{"catid":"11","upid":"8","catname":"html5 \u89c6\u9891\u6559\u7a0b"},{"catid":"12","upid":"8","catname":"jquery mobile \u6559\u7a0b"},{"catid":"13","upid":"8","catname":"js\/jquery \u6559\u7a0b"},{"catid":"14","upid":"8","catname":"css \u6559\u7a0b"},{"catid":"26","upid":"8","catname":"JqMobi \u89c6\u9891\u6559\u7a0b"},{"catid":"28","upid":"8","catname":"ionic \u6559\u7a0b"},{"catid":"29","upid":"8","catname":"angularjs\u6559\u7a0b"}]},{"catid":"15","upid":"0","catname":"\u79fb\u52a8\u4e92\u8054\u7f51","subcate":[]},{"catid":"20","upid":"0","catname":"PhoneGap\u8d44\u8baf","subcate":[]},{"catid":"25","upid":"0","catname":"phonegap100\u8d5e\u52a9\u89c6\u9891\u6559\u7a0b","subcate":[]},{"catid":"27","upid":"0","catname":"\u6742\u8c08","subcate":[]}]}
    return JsonResponse(mydict, safe = False) 

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

 

#  http://localhost:8000/wx_uploadFile/  
@csrf_exempt
def wx_uploadFile(request):
    name = '' 
    if request.method == 'POST':   
        myfile = request.FILES.get("file", None)                              
        if myfile:
            WriteFile(myfile)
            name = myfile.name 
        else:    
            if os.path.exists('name_img.jpg'):
                os.remove('name_img.jpg')
            name = 'None'         
    mylist = [{"name" : name}] 
    return JsonResponse(mylist, safe = False) 

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

   

