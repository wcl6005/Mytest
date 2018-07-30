# -*- coding: utf-8 -*-
import os
from django.shortcuts import render
try:
    import cStringIO as StringIO
except ImportError:
    import StringIO
import random
from django.shortcuts import render_to_response
from django.http import HttpResponse
from PIL import Image, ImageDraw, ImageFont, ImageFilter

FONT_TYPE = "static_common/home/fonts/DroidSans.ttf" 
_letter_cases = "abcdefghnpqrstuvxy".upper() 
_upper_cases = _letter_cases
_numbers = ''.join(map(str, range(3, 8)))
init_chars = ''.join((_letter_cases, _upper_cases, _numbers))

def get_chars(chars=init_chars, length=4):    
    return random.sample(chars, length)
def create_validate_code(request,size=(120, 30), mode="RGB",
                         bg_color=(255, 255, 255),
                         fg_color=(255, 0, 0),
                         font_size=22,
                         font_type=FONT_TYPE,
                         draw_lines=True,
                         n_line=(1, 3),
                         draw_points=True,
                         point_chance = 2):
    width, height = size 
    img = Image.new(mode, size, bg_color) 
    draw = ImageDraw.Draw(img) 

    def create_lines():
        line_num = random.randint(*n_line) 
        for i in range(line_num):
            begin = (random.randint(0, size[0]), random.randint(0, size[1]))
            end = (random.randint(0, size[0]), random.randint(0, size[1]))
            draw.line([begin, end], fill=(0, 0, 0))

    def create_points():
        chance = min(100, max(0, int(point_chance))) 

        for w in xrange(width):
            for h in xrange(height):
                tmp = random.randint(0, 100)
                if tmp > 100 - chance:
                    draw.point((w, h), fill=(0, 0, 0))

    def create_strs():
        c_chars =request.session['checkcode']
        strs = ' %s ' % ' '.join(c_chars) 
        font = ImageFont.truetype(font_type, font_size)
        font_width, font_height = font.getsize(strs)
        draw.text(((width - font_width) / 3, (height - font_height) / 3),
                  strs, font=font, fill=fg_color)
        return ''.join(c_chars)
    if draw_lines:
        create_lines()
    if draw_points:
        create_points()
    strs = create_strs()
    params = [1 - float(random.randint(1, 12)) / 100,
              0,
              0,
              0,
              1 - float(random.randint(1, 10)) / 100,
              float(random.randint(1, 2)) / 500,
              0.001,
              float(random.randint(1, 2)) / 500
    ]
    img = img.transform(size, Image.PERSPECTIVE, params) 
    img = img.filter(ImageFilter.EDGE_ENHANCE_MORE) 
    return img, strs

def checkcodeGIF(request):
    if not request.session.get('checkcode',''):
        request.session['checkcode'] = '1234'        
    img_type="GIF" 
    checkcode = create_validate_code(request)
    mstream = StringIO.StringIO()  
    checkcode[0].save(mstream, img_type) 
    codeImg = mstream.getvalue() 
    mstream.close()
    return  HttpResponse(codeImg, img_type) 

def gcheckcode(request):
    listchar = get_chars() 
    request.session['checkcode']=listchar
    return ''.join(listchar) 
     
# http://localhost:9000/home/getcheckcode/
def getcheckcode(request):
    g_checkcode = gcheckcode(request)
    path = request.GET.get('path')
    return  render(request, path, context=locals())

############################################################################### 
# def vueregister(request):
#     g_checkcode = gcheckcode(request)#验证码送前台验证
#     href = '/admin/auth/user/' #注册成功，重新定向
#     path = 'vue/register.html' #html路径
#     return  render(request, path , context=locals()) 


# <a  href="/home/getcheckcode/?path={{path}}" >  <!--注册后台-->
#     <img     src="/home/checkcodeGIF/"  alt="验证码图片" />
#                             看不清？换一个
# </a>