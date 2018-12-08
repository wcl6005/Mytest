import os
from django.shortcuts import render
from django.contrib import messages
from django.http.response import HttpResponseRedirect, HttpResponse

# http://localhost:8000/blog/index/
def index(request):
    return  render(request, 'blog/index.html', context=locals())

#上传单个文件。 http://localhost:8000/blog/upload/
def upload(request):  
    if request.method == "POST":    # 请求方法为POST时，进行处理  
        myFile =request.FILES.get("myfile", None)    # 获取上传的文件，如果没有文件，则默认为None  
        if not myFile:
            messages.info(request, '没有选择文件！')  
            return HttpResponseRedirect('#')   
        f = open(os.path.join("blog/static/upload",myFile.name),'wb+')    # 打开特定的文件进行二进制的写操作        
        for chunk in myFile.chunks():      # 分块写入文件  
            f.write(chunk)  
        f.close() 
        messages.info(request, myFile.name + '上传文件成功！浏览图像 /static/upload/%s'%(myFile.name))   
        return HttpResponseRedirect('/')     
    return  render(request, 'blog/upload.html', context=locals())

#上传目录(支持多个目录)中的所有文件。不能上传目录(结构)，只会把目录和其子目录的文件上传而不会上传目录。 http://localhost:8000/blog/upfolder/
def upfolder(request):  
    if request.method == "POST":    # 请求方法为POST时，进行处理  
        upimg =request.FILES.getlist("upimg", None)        #第一个目录 获取upimg文件列表
        upvideo =request.FILES.getlist("upvideo", None)    #第二个目录 获取upvideo文件列表
        
        writefile(request,upimg,'blog/static/upimg')        
        writefile(request,upvideo,'blog/static/upvideo')
    return  render(request, 'blog/upfolder.html', context=locals())

def writefile(request,upname,savepath):
    try:
        if not upname:
            messages.info(request, '没有选择目录！')  
            return HttpResponseRedirect('#')
        for file in upname:   
            position = os.path.join(savepath,str(file))
            f = open(position,'wb+')    # 打开特定的文件进行二进制的写操作        
            for chunk in file.chunks(): # 分块写入文件  
                f.write(chunk)  
            f.close()
        messages.info(request, '%s 所有文件上传成功!'%(upname))
    except Exception as ex:
        messages.info(request,str(ex))
    return HttpResponseRedirect('/')

