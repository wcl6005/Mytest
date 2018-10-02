# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http.response import HttpResponseRedirect, HttpResponse
from myAPI.videoURL import video_url_list

#观看视频网站 http://localhost:8000/dataacquisition/videoplay
def videoplay(request):
    url = ''
    line_list = video_url_list
    if request.method != 'POST':        
        return render(request, 'blog/videoplay.html', context=locals()) 
    cleanData = request.POST.dict()
    url = cleanData.get('url','')
    lineroad = cleanData.get('lineroad','')
    return render(request, 'blog/videoplay.html', context=locals())