# -*- coding: utf-8 -*-支持中文
# 文件名： checkcode.py
# 功能：内存显示图像验证码 模块  
# 目录下一定要有__init__.py文件，否则不能被其它文件引用、不能沿路径读写文件。from ... 。
import random
from PIL import Image, ImageDraw, ImageFont, ImageFilter

FONT_TYPE = "static_common/home/fonts/DroidSans.ttf" #相关字体文件. 当前目录 ../mysite
_letter_cases = "abcdefghnpqrstuvxy".upper() # 大写字母，去除可能干扰的i，l，o，z,j,m,w,k
_upper_cases = _letter_cases
_numbers = ''.join(map(str, range(3, 8))) # 数字
init_chars = ''.join((_letter_cases, _upper_cases, _numbers))

def get_chars(chars=init_chars, length=4): #length生成几位数的验证码    
    #生成给定长度的字符串，返回列表格式
    return random.sample(chars, length)
def create_validate_code(request,size=(120, 30), mode="RGB",
                         bg_color=(255, 255, 255),#背景白色
                         fg_color=(255, 0, 0),#字体红色
                         font_size=22,#字体大小
                         font_type=FONT_TYPE,# DroidSans.ttf 。放在工程目录
                         draw_lines=True,#是否要加入干扰线
                         n_line=(1, 3),#加入干扰线条数的上下限
                         draw_points=True,
                         point_chance = 2):
    width, height = size #图形 宽， 高
    img = Image.new(mode, size, bg_color) # 创建图形
    draw = ImageDraw.Draw(img) # 创建画笔

    def create_lines():
        #绘制干扰线
        line_num = random.randint(*n_line) # 干扰线条数
        for i in range(line_num):
            # 起始点
            begin = (random.randint(0, size[0]), random.randint(0, size[1]))
            #结束点
            end = (random.randint(0, size[0]), random.randint(0, size[1]))
            draw.line([begin, end], fill=(0, 0, 0))

    def create_points():
        #绘制干扰点
        chance = min(100, max(0, int(point_chance))) # 大小限制在[0, 100]

        for w in xrange(width):
            for h in xrange(height):
                tmp = random.randint(0, 100)
                if tmp > 100 - chance:
                    draw.point((w, h), fill=(0, 0, 0))

    def create_strs():
        #绘制验证码字符
        #c_chars = get_chars()
        c_chars =request.session['checkcode']
        strs = ' %s ' % ' '.join(c_chars) # 每个字符前后以空格隔开
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
    # 图形扭曲参数
    params = [1 - float(random.randint(1, 12)) / 100,
              0,
              0,
              0,
              1 - float(random.randint(1, 10)) / 100,
              float(random.randint(1, 2)) / 500,
              0.001,
              float(random.randint(1, 2)) / 500
    ]
    img = img.transform(size, Image.PERSPECTIVE, params) # 创建扭曲
    img = img.filter(ImageFilter.EDGE_ENHANCE_MORE) # 滤镜，边界加强（阈值更大）
    return img, strs



def gcheckcode(request):
    listchar = get_chars() #生成字符串（列表形式）
    request.session['checkcode']=listchar
    return ''.join(listchar) #列表形式字符串转换成字符串
     


