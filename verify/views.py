import random

import requests
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from . import models
import re, time
from django.contrib.auth.hashers import make_password, check_password


# Create your views here.

# 注册验证
@csrf_exempt
def register_verify(request):
  if request.method == "GET":
    return render(request, "signup.html", locals())
  elif request.method == "POST":
    rname = request.POST.get("username", "")
    password = request.POST.get("password", "")
    # 用户名约束  由2-10位字母、数字、下划线或中文组成，以字母或中文开头
    if not re.findall(r"^[\u4e00-\u9fa5a-zA-Z]{1}[\w]{1,9}$", rname):
      name_error = "用户名不符合规定"
      return render(request, "signup.html", locals())

    # 密码约束 由6-12位字母、数字组成
    if not re.match(r"^(?![0-9]+$)(?![a-zA-Z]+$)[0-9A-Za-z]{6,12}$", password):
      password_error = "密码不符合规定"
      return render(request, "signup.html", locals())
    password2 = request.POST.get("password2", "")
    if not password2 == password:
      password_error = "两次密码不一致"
      return render(request, "signup.html", locals())

    # 邮箱约束
    email = request.POST.get("email", "")
    # if not re.match(r"^[\.a-zA-Z0-9_-]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$", email):
    #   email_error = "无效邮箱"
    #   return render(request, "signup.html", locals())
    # if models.User.objects.filter(email=email):
    #   email_error = "邮箱已被注册"
    #   return render(request, "signup.html", locals())

    # 电话号码约束
    phone_number = request.POST.get("cell_verify", "")
    if not re.match(r"^1([38][0-9]|4[579]|5[0-3,5-9]|6[6]|7[0135678]|9[89])\d{8}", phone_number):
      code_error = "无效的手机号"
      return render(request, "signup.html", locals())
    # if models.User.objects.filter(phone_number=phone_number):
    #   code_error="手机号已被注册"
    #   return render(request, "signup.html", locals())

    # 手机短信验证
    code = request.POST.get("veri_code", "")
    try:
      veri_code = veri_info[0]
      veri_time = veri_info[1]
      veri_phone = veri_info[2]
    except:
      veri_error = '请求先获取验证码'
      return render(request, 'signup.html', locals())
    if code:
      if code != veri_code:  # 判断验证码是否正确
        veri_error = '验证码不正确'
        return render(request, 'signup.html', locals())
      if time.time() > veri_time + 300:
        veri_error = '验证码过期'
        return render(request, 'signup.html', locals())
    else:
      veri_error = "验证码不能为空"
      return render(request, 'signup.html', locals())

    # 验证用户名是否已存在
    try:
      n = models.User.objects.get(username=rname)
      print(n.username)
      name_error = "用户名已存在"
      return render(request, "signup.html", locals())
    except:
      # 密码加密
      password = make_password(password, "a", 'pbkdf2_sha1')

      models.User.objects.create(username=rname,
                                 password=password,
                                 mobile_number=phone_number,
                                 email=email)
      resp = HttpResponseRedirect("/verify/signin")
      resp.set_cookie("old_user", rname)
      return resp


# 发送手机短信
def get_code(request):
  phone_number = request.GET.get("phone_number", "")
  number = str(random.randrange(1000, 9999))  # 随机生成4位验证码
  global veri_info
  send_sms(number, phone_number)  # 调用send_sms函数
  veri_info = [number]
  veri_info.append(time.time())
  veri_info.append(phone_number)
  print(veri_info)
  return HttpResponse("1")


# 登录验证
@csrf_exempt
def sign_in(request):
  if request.method == "GET":
    username = request.COOKIES.get("old_user", "")
    return render(request, "login.html", locals())
  elif request.method == "POST":
    rname = request.POST.get("username", "null")
    password = request.POST.get("password", "null")

    # 用户名约束  由2-10位字母、数字、下划线或中文组成，以字母或中文开头
    if not re.findall(r"^[\u4e00-\u9fa5a-zA-Z]{1}[\w]{1,9}$", rname):
      name_error = "用户名不符合规定"
      return render(request, "login.html", locals())

    # 密码约束 由6-12位字母、数字组成
    if not re.match(r"^(?![0-9]+$)(?![a-zA-Z]+$)[0-9A-Za-z]{6,12}$", password):
      password_error = "密码不符合规定"
      return render(request, "login.html", locals())

    # 用户名和密码验证
    try:
      # 加密
      rpassword = make_password(password, "a", 'pbkdf2_sha1')
      auser = models.User.objects.get(username=rname, password=rpassword)
    except:
      password_error = "用户名或密码错误"
      return render(request, "login.html", locals())

    # 用户名密码正确，在session里标记用户为登陆状态
    request.session["user"] = {
      "name": auser.username,
      "id": auser.id
    }

    # 设置cookie
    is_remember = request.POST.get("remember", "")
    # resp=render(request,"main.html",locals())
    resp = HttpResponseRedirect("/chat/index")
    if is_remember == "1":
      resp.set_cookie("old_user", rname)
    else:
      resp.delete_cookie("old_user")
    return resp


# 手机短信验证API
def send_sms(number, mobile):
  url = "http://106.ihuyi.com/webservice/sms.php?method=Submit"  # 请求地址
  account = "C23589526"  # 提交账户APIID
  password = "b4915e164e86723594356e4855a9bb62"  # 提交密码APIKEY

  # 请求的头部
  headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
  # 数据整合 请求数据必须为字典类型
  data = {
    "account": account,
    "mobile": mobile,
    "password": password,
    "content": "您的验证码是：" + number + "。请不要把验证码泄露给其他人。"  # 发送的验证码短信，要注意符合模板格式，不然无法发送成功
  }
  # 发起请求
  response = requests.post(url=url, data=data, headers=headers)
  # 接收返回内容
  result = response.content.decode()
  print(result)
  result2 = re.findall(r'<msg>(.*)</msg>', result)[0]
  return result2


# 个人设置
@csrf_exempt
def personal_set(request):
  return render(request, 'personal_set.html')

# 忘记密码的验证
def pwd_reset(request):
  if request.method == "GET":
    return render(request, 'password_reset.html')
  elif request.method == "POST":
    code=request.POST.get("veri_code")
    try:
      veri_code = veri_info[0]
      veri_time = veri_info[1]
      print(code,veri_code)
    except:
      veri_error = '请求先获取验证码'
      return render(request, 'password_reset.html', locals())
    if code:
      if code != str(veri_code):  # 判断验证码是否正确
        veri_error = '验证码不正确'
        return render(request, 'password_reset.html', locals())
      if time.time() > veri_time + 300:
        veri_error = '验证码过期'
        return render(request, 'password_reset.html', locals())
    print("sfsf")
    return render(request, 'password_reset2.html')

# 忘记密码的修改密码
def pwd_reset2(request):
  if request.method == "GET":
    return render(request, 'password_reset2.html')
  elif request.method == "POST":
    password1 = request.POST.get("password", "")
    password2 = request.POST.get("password2", "")
    if password1 != password2:
      password_error = "两次密码不一致"
      return render(request, 'password_reset2.html', locals())
    # 密码约束 由6-12位字母、数字组成
    if not re.match(r"^(?![0-9]+$)(?![a-zA-Z]+$)[0-9A-Za-z]{6,12}$", password1):
      password_error = "密码不符合规定"
      return render(request, 'password_reset2.html', locals())
    # 加密
    rpassword = make_password(password1, "a", 'pbkdf2_sha1')
    # 修改密码
    # user = models.User.objects.filter(mobile_number=veri_info[2])[0]
    user = models.User.objects.filter(mobile_number="18720988525")[0]
    user.password = rpassword
    user.save()
    return HttpResponseRedirect("/verify/signin")
