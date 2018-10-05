# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http.response import HttpResponseRedirect, HttpResponse
from myAPI.videoURL import video_url_list
from blog.models import Video, Browse

#观看视频网站 http://localhost:9000/blog/videoplay
def videoplay(request):
    url = ''
    line_list = video_url_list
    Browse.objects.filter().update(computer=str(int(Browse.objects.get().computer)+1))
    if request.method != 'POST':        
        l = 1
        lineroad = line_list[0]
        return render(request, 'blog/videoplay.html', context=locals()) 
    cleanData = request.POST.dict()
    url = cleanData.get('url','').strip()
    lineroad = cleanData.get('lineroad','').strip()
    l = line_list.index(lineroad) + 1
    return render(request, 'blog/videoplay.html', context=locals())

# http://localhost:9000/blog/vipplay
def vipplay(request):
    if request.method != 'POST':
        videos = Video.objects.values()
        return render(request, 'blog/vipplay.html', context=locals())
    Browse.objects.filter().update(mobilephone=str(int(Browse.objects.get().mobilephone)+1))
    cleanData = request.POST.dict()
    url = cleanData.get('url','').strip()
    name = cleanData.get('name','').strip()
    tvname = cleanData.get('tvname','').strip()
    if '爱奇艺' in tvname:
        lineroad = video_url_list[4] #线路5
    else:    
        lineroad = video_url_list[0] #线路1 
    return render(request, 'blog/vipplay.html', context=locals())
