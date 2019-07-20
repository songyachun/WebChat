from django.http import HttpResponse
from django.shortcuts import render

def login_view(request):
    # if request.method=='GET':
    #     return render(request,'index.html')
    # elif request.method =='POST':
    #     name=request.POST.get('name')
    #     password= request.POST.get('password')
    return render(request,'login.html')


def signup_view(request):
    return render(request, 'signup.html')

def chat(request):
    return HttpResponse('登录成功！')

def user_add_view(request):
    return HttpResponse('添加用户数据成功！')

def main_view(request):
    return render(request,'main.html')