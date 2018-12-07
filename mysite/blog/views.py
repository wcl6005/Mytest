import os
from django.shortcuts import render
from django.contrib import messages
from django.http.response import HttpResponseRedirect, HttpResponse

# http://localhost:8000/blog/index/
def index(request):
    return  render(request, 'blog/index.html', context=locals())

# http://localhost:8000/blog/upload/
def upload(request):  
    if request.method == "POST":    # 请求方法为POST时，进行处理  
        myFile =request.FILES.get("myfile", None)    # 获取上传的文件，如果没有文件，则默认为None  
        if not myFile:
            messages.info(request, '上传没有文件！')  
            return HttpResponseRedirect('#')   
        f = open(os.path.join("mysite/blog/static/upload",myFile.name),'wb+')    # 打开特定的文件进行二进制的写操作        
        for chunk in myFile.chunks():      # 分块写入文件  
            f.write(chunk)  
        f.close() 
        messages.info(request, myFile.name + '上传文件成功！浏览图像 /static/upload/%s'%(myFile.name))   
        return HttpResponseRedirect('/')
     
    return  render(request, 'blog/upload.html', context=locals())