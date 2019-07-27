from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt,csrf_protect
from . import models
import re
from django.contrib.auth.hashers import make_password, check_password

# Create your views here.

# 注册验证
@ csrf_exempt
def register_verify(request):
  if request.method == "GET":
    return render(request, "signup.html", locals())
  elif request.method == "POST":
    rname = request.POST.get("username", "")
    password = request.POST.get("password", "")
    # 用户名约束  由2-10位字母、数字、下划线或中文组成，以字母或中文开头
    if not re.findall(r"^[\u4e00-\u9fa5a-zA-Z]{1}[\w]{1,9}$", rname):
      name_error="用户名不符合规定"
      return render(request,"signup.html",locals())

    # 密码约束 由6-12位字母、数字组成
    if not re.match(r"^(?![0-9]+$)(?![a-zA-Z]+$)[0-9A-Za-z]{6,12}$", password):
      password_error="密码不符合规定"
      return render(request, "signup.html", locals())

    # 电话号码约束
    phone_number= request.POST.get("cell_verify", "")
    if not re.match(r"^1([38][0-9]|4[579]|5[0-3,5-9]|6[6]|7[0135678]|9[89])\d{8}",phone_number):
      phone_error="无效的手机号"
      return render(request, "signup.html", locals())

    # 邮箱约束
    email=request.POST.get("email", "")
    if not re.match(r"^[a-zA-Z0-9_-]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$",email):
      email_error="无效邮箱"
      return render(request, "signup.html", locals())

    # 验证用户名是否已存在
    try:
      n=models.User.objects.get(username=rname)
      print(n.username)
      name_error="用户名已存在"
      return render(request,"signup.html",locals())
    except:
      # 密码加密
      password = make_password(password, "a", 'pbkdf2_sha1')

      models.User.objects.create(username=rname,
                                 password=password,
                                 mobile_number=phone_number,
                                 email=email)
      resp= HttpResponseRedirect("/verify/signin")
      resp.set_cookie("old_user",rname)
      return resp

# 登录验证
@ csrf_exempt
def sign_in(request):
  if request.method=="GET":
    username=request.COOKIES.get("old_user","")
    return render(request,"login.html",locals())
  elif request.method == "POST":
    rname = request.POST.get("username", "null")
    password = request.POST.get("password", "null")

    # 用户名约束  由2-10位字母、数字、下划线或中文组成，以字母或中文开头
    if not re.findall(r"^[\u4e00-\u9fa5a-zA-Z]{1}[\w]{1,9}$", rname):
      name_error="用户名不符合规定"
      return render(request,"login.html",locals())

    # 密码约束 由6-12位字母、数字组成
    if not re.match(r"^(?![0-9]+$)(?![a-zA-Z]+$)[0-9A-Za-z]{6,12}$", password):
      password_error = "密码不符合规定"
      return render(request, "login.html", locals())

    # # 电话号码约束
    # if not re.match(r"^1([38][0-9]|4[579]|5[0-3,5-9]|6[6]|7[0135678]|9[89])\d{8}",phone_number):
    #   return HttpResponse("无效的手机号")
    #
    # # 邮箱约束
    # if not re.match(r"^[a-zA-Z0-9_-]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$",email):
    #   return HttpResponse("无效邮箱")

    # 用户名和密码验证
    try:
      # 加密
      rpassword = make_password(password, "a", 'pbkdf2_sha1')
      auser=models.User.objects.get(username=rname, password=rpassword)
    except:
      password_error="用户名或密码错误"
      return render(request, "login.html", locals())

    # 用户名密码正确，在session里标记用户为登陆状态
    request.session["user"] = {
      "name": auser.username,
      "id": auser.id
    }

    # 设置cookie
    is_remember=request.POST.get("remember","")
    # resp=render(request,"main.html",locals())
    resp=HttpResponseRedirect("/chat/index")
    if is_remember=="1":
      resp.set_cookie("old_user",rname)
    else:
      resp.delete_cookie("old_user")
    return resp

  #个人设置
  # @csrf_exempt
def personal_set(request):
  return render(request,'personal_set.html')