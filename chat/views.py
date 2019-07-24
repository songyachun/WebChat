from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse

# Create your views here.

# 函数装饰器，检查用户是否登入，没有登入跳转登入页面
def check_login(fn):
  def warp(request, *args, **kwargs):
    if "user" not in request.session:
      return HttpResponseRedirect("/verify/signin")  # 返回登录界面
    else:
      return fn(request, *args, **kwargs)
  return warp

@ check_login
def chat(request):
  if request.method=="GET":
    # username=request.COOKIES.get("old_user","")
    return render(request,"main.html",locals())