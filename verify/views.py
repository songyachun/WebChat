from django.shortcuts import render
from django.http import HttpResponse
from . import models
import re

from werkzeug.security import generate_password_hash

# Create your views here.

# 注册验证
def register_verify(request):
  if request.method == "POST":
    rname = request.POST.get("name", "null")
    password = request.POST.get("password", "null")
    # 密码加密
    password = generate_password_hash(password)

    # 用户名约束  由2-10位字母、数字、下划线或中文组成，以字母或中文开头
    if not re.findall(r"^[a-zA-Z]{1}[\w]{1,9}$", rname):
      return HttpResponse("用户名错误")

    # 用户名查重
    names = models.UserInfo.objects.values("username")
    for name in names:
      if name["username"] == rname:
        return HttpResponse("注册失败")
    else:
      models.UserInfo.objects.create(username=rname, password=password)
      return HttpResponse("注册成功")


# 登录验证
def sign_in(request):
  if request.method == "POST":
    rname = request.POST.get("name", "null")
    rpassword = request.POST.get("password", "null")
    # 获得姓名列，密码列
    infos = models.UserInfo.objects.values("username", "password")
    # name为字典格式
    for user in infos:
      if user["username"] == rname and user["password"] == rpassword:
        return HttpResponse("登入成功")
    else:
      return HttpResponse("用户名或密码错误")
