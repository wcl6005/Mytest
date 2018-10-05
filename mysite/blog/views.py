# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http.response import HttpResponseRedirect, HttpResponse
from myAPI.videoURL import video_url_list

#观看视频网站 http://localhost:9000/blog/videoplay
def videoplay(request):
    url = ''
    line_list = video_url_list
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
    cleanData = request.POST.dict()
    url = cleanData.get('url','').strip()
    name = cleanData.get('name','').strip()
    if 'www.iqiyi.com' in url:
        if 'v_19rr05tu6s' in url  or \
            'v_19rrhl4urg' in url  or \
            'v_19rroi2pgs' in url:
            lineroad = video_url_list[5] #线路6
        elif 'v_19rrn70w8c' in url:
            lineroad = video_url_list[2]  #线路3
        else:
            lineroad = video_url_list[4] #线路5

    return render(request, 'blog/vipplay.html', context=locals())