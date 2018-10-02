# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http.response import HttpResponseRedirect, HttpResponse

video_url_list = ["http://www.wmxz.wang/video.php?url=",
        "https://www.jqaaa.com/jx.php?url=", #0
        "https://5.5252e.com/jx/b.php?url=",
        "http://yun.mt2t.com/yun?url=",                   
        "http://api.bbbbbb.me/yunjx/?url=",        
        "http://000o.cc/jx/ty.php?url=",
        "http://api.baiyug.cn/vip/index.php?url=", #6 le电视剧、爱奇艺
        "http://yun.baiyug.cn/vip/?url=",
];
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