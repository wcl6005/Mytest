from django.shortcuts import render
from django.contrib.auth import login as auth_login #当函数名是login，必须用auth_login
from django.contrib.auth import authenticate #django验证登录
from django.http.response import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User


# Create your views here.

def index0(request):
    return  render(request, 'define_menu/index0.html', context=locals())

def index1(request):
    return  render(request, 'blog/index1.html', context=locals())
def index2(request):
    return  render(request, 'blog/index2.html', context=locals())

def index3(request):
    return  render(request, 'index3/index3.html', context=locals())


def login(request):
    if request.method != 'POST':
        return  render(request, 'blog/login.html', context=locals()) 
    username = request.POST['username']
    password = request.POST['password']
    href = request.POST['href']
    if href == '':  href = '/' #href空，转index
    user = authenticate(username=username, password=password) #django验证登录
    if user: 
        auth_login(request, user)
        return  HttpResponseRedirect(href)
    messages.info(request, u'登录失败！请输入一个正确的 用户名 和密码. 注意他们都是区分大小写的！')
    return  render(request, 'blog/login.html', context=locals())

def register(request):
    if request.method != 'POST':
        return  render(request, 'blog/register.html', context=locals())      
    name = request.POST['username']
    isname = User.objects.filter(username = name)
    if isname:  #判断name是否有相同的记录
        messages.info(request, name + '用户已经注册！')
        return HttpResponseRedirect('#')   
    email = request.POST['email']
    password = request.POST['password']
    user = User.objects.create_user(name, email, password) #用户,不能从Django自带登录界面，登录
    user.is_staff = False #非职员 默认False
    user.is_superuser = False #非超级用户 默认False
    user.save()
    auth_login(request, user)
    return  HttpResponseRedirect('/')    
