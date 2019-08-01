import os

from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
import pymysql
from verify import models, views
from webchat import settings



# Create your views here.

# 函数装饰器，检查用户是否登入，没有登入跳转登入页面
def check_login(fn):
    def warp(request, *args, **kwargs):
        if "user" not in request.session:
            return HttpResponseRedirect("/verify/signin")  # 返回登录界面
        else:
            return fn(request, *args, **kwargs)

    return warp


@check_login
def chat(request):
    if request.method == "GET":
        # 邮箱链接
        email_address_dict = {
            "163.com": "https://mail.163.com/",
            "qq.com": "https://mail.qq.com/"
        }
        username = request.session["user"]["name"]
        user = models.User.objects.filter(username=username)
        email_sign = re.findall(r"@(.*)", user[0].email)
        print(email_sign)
        email_link = email_address_dict[email_sign[0]]

        # 爬虫相关设置
        ip = request.META['REMOTE_ADDR']
        # print(ip)
        weather = get_weather(ip)
        news_list = get_news()
        return render(request, "main.html", locals())


# 修改密码
def mod_pwd(request):
    if request.method == 'POST':
        try:
            username = request.session["user"]["name"]
            user = models.User.objects.filter(username=username)
        except:
            return HttpResponse('用户未登录')
        # 修改密码
        # 输入的旧密码old_pwd，新密码new_pwd1,new_pwd2
        old_pwd = request.POST.get('old_pwd')
        new_pwd1 = request.POST.get('new_pwd1')
        new_pwd2 = request.POST.get('new_pwd2')

        # 密码约束 由6-12位字母、数字组成
        if not re.match(r"^(?![0-9]+$)(?![a-zA-Z]+$)[0-9A-Za-z]{6,12}$", new_pwd1):
            new_pwd_error = "密码不符合规定"
            return render(request, "password_reset2.html", locals())

        old_pwd = views.make_password(old_pwd, "a", 'pbkdf2_sha1')
        if models.User.password == old_pwd:
            if new_pwd1 == new_pwd2:
                new_pwd2 = views.make_password(new_pwd2, "a", 'pbkdf2_sha1')
                user.password = new_pwd2
                user.save()
            else:
                new_pwd_error = '新密码输入不一致'
                return render(request, 'password_reset2.html', locals())
        else:
            old_pwd_error = '旧密码输入错误'
            return render(request, 'password_reset2.html', locals())


# 修改昵称 年龄　生日　地址　电子邮件　电话号码
def mod_nickname(request):
    if request.method == 'POST':
        try:
            username = request.session["user"]["name"]
            user = models.User.objects.filter(username=username)

        except:
            return HttpResponse('用户未登录')

        new_email = request.POST.get('email', '')
        new_phone_number = request.POST.get('phone_number', '')

        new_nickname = request.POST.get('nickname', '')
        new_age = request.POST.get('age', '')
        new_bithday = request.POST.get('bithday', '')
        new_address = request.POST.get('address', '')

        # 创建UserInfo关联User,得到当前的User对应的UserInfo信息
        userinfo = models.UserInfo.objects.create()

        # 修改信息
        # User表
        user.email = new_email
        user.mobile_number = new_phone_number
        user.save()
        # UserInfo表
        userinfo.nickname = new_nickname
        userinfo.age = new_age
        userinfo.bithday = new_bithday
        userinfo.address = new_address
        userinfo.save()


# 上传头像
def upload_avatar(request):
    if request.method == "POST":
        try:
            username = request.session["user"]["name"]
            user = models.User.objects.filter(username=username)
        except:
            return HttpResponse('用户未登录')

        file = request.FILES['myfile']
        print("上传文件名是:", file.name)

        filename = os.path.join(settings.MEDIA_ROOT, file.name)
        with open(filename, 'wb') as f:
            f.write(file.file.read())
            return HttpResponse("接收文件成功")
        # 数据库要存储头像路径



import requests
import re


# 查询数据库,返回城市对应的编码
def get_city_code(city):
    # 连接数据库,charset参数必填
    conn = pymysql.connect(host='localhost',
                           port=3306,
                           user='root',
                           password='123456',
                           database='webchat_db',
                           charset="utf8")
    cursor = conn.cursor()
    sql = '''select code from city_code where city="%s";''' % (city)
    cursor.execute(sql)
    # 查询结果
    city_code = cursor.fetchone()
    if not city_code:
        return 101280601
    conn.close()
    return city_code[0]


def get_city(ip):
    url = "http://ip.tool.chinaz.com/?IP={}".format(ip)
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"}
    responses = requests.get(url, headers=headers)
    context = responses.content.decode("utf-8")
    city = re.findall(r'span class="Whwtdhalf w50-0">.*?省(\w+?)市.*?</span>', context)
    print(city)
    return city[0]


# 根据客户端ip获取天气
def get_weather(ip):
    try:
        city = get_city(ip)
    except:
        city = "深圳"
    url = "http://www.weather.com.cn/weather1d/{}.shtml".format(get_city_code(city))
    response = requests.get(url)
    response.encoding = 'utf-8'
    # 抓取当天气温（非实时）
    aim = re.findall('<input type="hidden" id="hidden_title" value=".*?\w{2}  (.*?)  (.*?)"',
                     response.text, re.S)
    print("今日气温：%s %s" % aim[0])
    return aim[0]


def get_news():
    news_list = []
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"}
    url = "http://www.xinhuanet.com/politics/"
    response = requests.get(url, headers=headers)
    text = response.content.decode('utf-8')
    # 初步过滤
    info = re.findall(r'<div class="wrap">.*?</a></div>', text)
    # 获得五条新闻
    n = 0
    for i in info:
        url_img = re.findall(r'data-original=(.*?) /> ', i)
        url_html = re.findall(r'<a href="(.*?)" target="_blank">', i)
        title = re.findall(r'_blank">(.*?)</a></div>', i)
        news_list.append(url_img + url_html + title)
        n += 1
        if n > 4:
            return news_list


if __name__ == "__main__":
    get_weather("深圳")
    print(get_city_code("深圳"))
    print(get_news())
    get_city("118.212.211.13")
# <p class="tem on">最高气温: 33℃ , 最低气温: 26℃</p>
