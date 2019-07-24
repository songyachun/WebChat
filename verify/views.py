from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from . import models
import re, requests, random
from django.contrib.auth.hashers import make_password, check_password


# Create your views here.

# 注册验证
@csrf_exempt
def register_verify(request):
    if request.method == "GET":
        return render(request, "signup.html", locals())
    elif request.method == 'POST':
        rname = request.POST.get("username", "")
        password = request.POST.get("password", "")
        email = request.POST.get("email", "")
        password2=request.POST.get('password2','')
        #手机验证码验证
        if 'getCode' in request.POST:
            mobile = request.POST.get('cell_verify', '')  # 获取手机号码
            number = str(random.randrange(1000, 9999))  # 随机生成4位验证码
            mobile_error = send_sms(number, mobile)  # 调用send_sms函数
            code=request.POST.get('code_verify','')
            if code!=number:                         #判断验证码是否正确
                code_error='验证码不正确'
                return render(request,'signup.html',locals())

        # 用户名约束  由2-10位字母、数字、下划线或中文组成，以字母或中文开头
        if not re.findall(r"^[\u4e00-\u9fa5a-zA-Z]{1}[\w]{1,9}$", rname):
            name_error = "用户名不符合规定"
            return render(request, "signup.html", locals())

        # 密码约束 由6-12位字母、数字组成
        if not re.match(r"^(?![0-9]+$)(?![a-zA-Z]+$)[0-9A-Za-z]{6,12}$", password):
            password_error = "密码不符合规定"
            return render(request, "signup.html", locals())

        # 电话号码约束
        phone_number = request.POST.get("cell_verify", "")
        if not re.match(r"^1([38][0-9]|4[579]|5[0-3,5-9]|6[6]|7[0135678]|9[89])\d{8}", phone_number):
            phone_error = "无效的手机号"
            return render(request, "signup.html", locals())

        # 邮箱约束

        if not re.match(r"^[a-zA-Z0-9_-]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$", email):
            email_error = "无效邮箱"
            return render(request, "signup.html", locals())

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


        # 邮箱约束
        if not re.match(r"^[a-zA-Z0-9_-]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$",email):
          return HttpResponse("无效邮箱")

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

    # 接口类型：互亿无线触发短信接口，支持发送验证码短信、订单通知短信等。
    # 账户注册：请通过该地址开通账户http://user.ihuyi.com/register.html
    # 注意事项：
    # （1）调试期间，请使用用系统默认的短信内容：您的验证码是：【变量】。请不要把验证码泄露给其他人。
    # （2）请使用 APIID 及 APIKEY来调用接口，可在会员中心获取；
    # （3）该代码仅供接入互亿无线短信接口参考使用，客户可根据实际需要自行编写；

    # !/usr/local/bin/python
    # -*- coding:utf-8 -*-

    # 查看用户名 登录用户中心->验证码通知短信>产品总览->API接口信息->APIID

    # 查看密码 登录用户中心->验证码通知短信>产品总览->API接口信息->APIKEY


def send_sms(number, mobile):
    url = "http://106.ihuyi.com/webservice/sms.php?method=Submit"  # 请求地址
    mobile = mobile

    account = "C98838401"  # 提交账户APIID

    password = "c67a2d2c06d362e33711c4a33ac6ba29"  # 提交密码APIKEY

    # 请求的头部
    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}

    # 数据整合
    data = {
        "account": account,
        "mobile": mobile,
        "password": password,
        "content": "您的验证码是：" + number + "。请不要把验证码泄露给其他人。"  # 发送的验证码短信，要注意符合模板格式，不然无法发送成功
    }  # 请求数据必须为字典类型
    # 发起请求
    response = requests.post(url=url, data=data, headers=headers)
    # 接收返回内容
    result = response.content.decode()
    result2 = re.findall(r'<msg>(.*)</msg>', result)[0]
    return result2


