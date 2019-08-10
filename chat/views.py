import os
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
import pymysql
import json
from verify import models
import requests
import re, time
from dwebsocket import require_websocket
from dwebsocket import accept_websocket
from dwebsocket.websocket import WebSocket
from verify import models, views
from webchat import settings
from verify.views import csrf_exempt
from verify.models import User, Messages, MessagesType, UserInfo


# 函数装饰器，检查用户是否登入，没有登入跳转登入页面
def check_login(fn):
  def warp(request, *args, **kwargs):
    if "user" not in request.session:
      # 返回登录界面
      return HttpResponseRedirect("/verify/signin")
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
    # email_link = email_address_dict[email_sign[0]]

    # 爬虫相关设置
    ip = request.META['REMOTE_ADDR']
    # print(ip)
    weather = get_weather(ip)
    news_list = get_news()
    return render(request, "main.html", locals())


# 修改密码
@check_login
def mod_pwd(request):
  if request.method == 'GET':
    username = request.session["user"]["name"]
    return render(request, 'change_password.html', locals())
  if request.method == 'POST':
    try:
      username = request.session["user"]["name"]
      user = models.User.objects.filter(username=username)
    except:
      return HttpResponse('用户未登录')

    # 修改密码
    # 输入的旧密码old_pwd，新密码new_pwd1,new_pwd2
    old_pwd = request.POST.get('old_password')
    new_pwd1 = request.POST.get('password1')
    new_pwd2 = request.POST.get('password2')

    # 密码约束 由6-12位字母、数字组成
    if not re.match(r"^(?![0-9]+$)(?![a-zA-Z]+$)[0-9A-Za-z]{6,12}$", new_pwd1):
      new_pwd_error = "密码不符合规定"
      return render(request, "change_password.html", locals())

    old_pwd = views.make_password(old_pwd, "a", 'pbkdf2_sha1')
    if user.password == old_pwd:
      if new_pwd1 == new_pwd2:
        new_pwd2 = views.make_password(new_pwd2, "a", 'pbkdf2_sha1')
        user.password = new_pwd2
        print('***********************')
        print('user.password', user.password)
        print('***********************')

        user.save()
        return HttpResponse(0)
      else:
        new_pwd_error = '新密码输入不一致'
        return render(request, 'change_password.html', locals())
    else:
      old_pwd_error = '旧密码输入错误'
      return render(request, 'change_password.html', locals())


def inter_layout(request):
  return render(request, 'inter_layout.html')


def feedback(request):
  return render(request, 'feedback.html')


# 修改昵称 年龄　生日　地址　电子邮件　电话号码
@csrf_exempt
def mod_user_info(request):
  if request.method == 'GET':
    username = request.session["user"]["name"]
    return render(request, 'personal_set.html', locals())
  if request.method == 'POST':
    try:
      username = request.session["user"]["name"]
      user = models.User.objects.filter(username=username)[0]
      print(user.id)

    except:
      return HttpResponse('用户未登录')

    new_email = request.POST.get('mail', '')
    sex = request.POST.get('gender', '')
    nickname = request.POST.get('nickname', '')
    age = request.POST.get('age', '')
    birthday = request.POST.get('birthday', '')
    phone_num = request.POST.get('phone_num', '')
    address = request.POST.get('address', '')
    per_sign = request.POST.get('per_sign', '')
    # 查看接收到的数据
    print("****************")
    print('new_email:', new_email)
    print('sex:', sex)
    print('nickname:', nickname)
    print('age:', age)
    print('birthday:', birthday)
    print('phone_num:', phone_num)
    print('address:', address)
    print('per_sign:', per_sign)
    print("****************")

    # 修改信息
    # User表
    # 数据库为空则添加否则修改
    if not models.User.email or not models.User.mobile_number:
      models.User.objects.create(email=new_email)
      models.User.mobile_number.objects.create(mobile_number=phone_num)
    else:
      user.email = new_email
      user.mobile_number = phone_num
      user.save()
      # return HttpResponse('1')

    # UserInfo表
    # 数据转换boy->1 gril->0
    if sex == 'boy':
      sex = 1
    else:
      sex = 0

    # 实例化Province一个城市对象
    province = models.Province.objects.create(P_name=address)
    city = models.City.objects.create(
      C_Name='11',
      P_ProcvinceID=province)

    # 用户有信息则修改,没有则创建
    try:
      userinfo = models.UserInfo.objects.get(user=user)
      userinfo.nickname = nickname
      userinfo.age = age
      userinfo.bithday = birthday
      userinfo.sex = sex
      userinfo.save()
    except:
      pass
      userinfo = models.UserInfo.objects.create(
        nickname=nickname,
        sex=sex,
        age=age,
        birthday=birthday,
        province_id=province,
        user=user,  # 增加一对一属性
        city_id=city,

      )

    return HttpResponse('1')


# 上传头像
@csrf_exempt
def upload_avatar(request):
  if request.method == 'GET':
    username = request.session["user"]["name"]
    return render(request, 'personal_set.html', locals())
  if request.method == "POST":
    try:
      username = request.session["user"]["name"]
      user = models.User.objects.filter(username=username)
    except:
      return HttpResponse('用户未登')

    avatar = request.FILES.get('avatar')
    # 写入头像文件到static/avatar
    filename = os.path.join(settings.MEDIA_ROOT, avatar.name)
    with open(filename, 'wb') as f:
      f.write(avatar.file.read())
    print('avatar', avatar)
    user.avatar = avatar
    user.save()
    return HttpResponse("1")


# 刷新天气
def city_weather(request):
  city = request.GET.get('city', '')
  print(city)
  url = "http://www.weather.com.cn/weather1d/{}.shtml".format(get_city_code(city))
  response = requests.get(url)
  response.encoding = 'utf-8'
  aim = re.findall('<input type="hidden" id="hidden_title" value=".*?\w{2}  (.*?)  (.*?)"',
                   response.text, re.S)
  # tem = aim[0][1]
  # des = aim[0][0]
  # dic = {'tem':tem,'des':des}
  resText = json.dumps(aim[0])
  print(resText)
  return HttpResponse(resText)


def send_message(request):
  if request.method == "GET":
    return render(request, "test.html")


# 发送好友列表
def send_friend_list(request, user_id):
  friend_list = {'code': 200, "friends": []}
  user_query = User.objects.filter(username=user_id)[0]
  friends_send = user_query.friends.all()
  friends_recive = User.objects.filter(friends=user_query)
  # 两个列表的并集
  friends_query=list(set(friends_send).union(set(friends_recive)))
  if len(friends_query):
    for user in friends_query:
      friends = {}
      friends["username"]= user.username
      friends["nickname"] = user.userinfo.nickname
      friends["sex"] = user.userinfo.sex
      friends["age"] = user.userinfo.age
      friends["birthday"] = user.userinfo.birthday
      friends["profile_head"] = str(user.userinfo.profile_head)
      friends["profile"] = user.userinfo.profile
      friend_list['friends'].append(friends)
  friend_list = json.dumps(friend_list).encode()
  request.websocket.send(friend_list)



# 登陆者接收离线信息
def recive_offline_msg(request,user_id,client_list):
  loginer=User.objects.filter(username=user_id)[0]
  ms_unsend = Messages.objects.filter(M_status=False,
                                      M_ToUserID=loginer)
  for ms in ms_unsend:
    # 获取消息类型
    ms_type=ms.M_MessagesTypeID.MT_Name
    # 好友请求类型
    if ms_type=="0":
      pass
    # 应答好友请求类型
    elif ms_type=="1":
      pass

# 处理未发送的消息
def send_unsend_msg(client_list,dataType_query,messages):
  # 找到未发送的好友请求信息
  ms_unsend = Messages.objects.filter(M_status=False,
                                      M_MessagesTypeID=dataType_query)
  # 遍历发送
  for i in ms_unsend:
    print("==step1.1==", i.M_ToUserID.username)
    # 判断接收者是否登录
    if i.M_ToUserID.username in client_list.keys():
      if not client_list[i.M_ToUserID.username].is_closed():
        # print("==step1.2==", messages)
        messages["step"] = "1"
        messages = json.dumps(messages)
        client_list[i.M_ToUserID.username].send(messages.encode())
        # 标记已发送的消息
        i.M_status = True
        i.save()
        print("===step1.3===", i.M_status)

# 处理添加好友请求
client_list = {}
@accept_websocket
def add_friend(request):
  if request.is_websocket():
    # 记录连接的客户端
    user_id = request.session["user"]["name"]
    client_list[user_id] = request.websocket
    print(client_list)
    # 发送好友列表
    send_friend_list(request, user_id)

    # 接收离线信息
    # recive_offline_msg(request,user_id,client_list)

    for messages in request.websocket:
      messages = json.loads(messages.decode())
      print("===messages===",messages)

      # 获取messages
      step = messages.get("step")
      sender = messages.get("sender")
      sender_query = User.objects.filter(username=sender)
      # 判断发送者和接收者是否存在
      if not sender_query:
        request.websocket.send(b'{"code":101,"error":"The sender is not existed"}')
        continue
      reciver = messages.get("reciver")
      reciver_query = User.objects.filter(username=reciver)
      if not reciver_query:
        request.websocket.send(b'{"code":102,"error":"The reciver is not existed"}')
        continue
      dataType = messages.get("dataType")
      print(dataType)
      dataType_query = MessagesType.objects.filter(MT_Name=str(dataType))
      if not dataType_query:
        request.websocket.send(b'{"code":102,"error":"The dataType is not existed"}')
        continue

      # 接收申请请求
      if step == 0:
        print("====step0====",messages)
        # 阻止好友请求重复发送
        if not Messages.objects.filter(M_FromUserID=sender_query[0],
                                       M_ToUserID=reciver_query[0],
                                       M_status=False):
          # 添加消息
          Messages.objects.create(M_status=False,
                                  M_MessagesTypeID=dataType_query[0],
                                  M_FromUserID=sender_query[0],
                                  M_ToUserID=reciver_query[0],
                                  M_PostMessages=json.dumps(messages)
                                  )

        else:
          request.websocket.send(b'{"code":103,"error":"Donot send friend_request double"}')
        step = 1
      # 发送申请响应
      if step == 1:
        send_unsend_msg(client_list,dataType_query[0],messages)

      # 接收应答请求
      if step == 2:
        status = messages.get("status")
        if status == "1":
          sender_query[0].friends.add(reciver_query[0])
          sender_query[0].save()

          print("==step2==")
          # request.websocket.send(b'{"code":105,"error":"The user been add friend alreadly"}')
        else:
          print("%s拒绝好友请求%s" % (reciver, sender))
        step = 3
      # 发送应达响应
      if step == 3:
        print("===step3===",messages)
        # 客户端在线时发送
        print("===step3.1===在线？", client_list[reciver_query[0].username].is_closed())
        if not client_list[reciver_query[0].username].is_closed():
          messages=json.dumps(messages).encode()
          client_list[sender].send(messages)
        # 对方不在线时存储
        else:
          print("===step3.1===存储",messages)
          Messages.objects.create(M_status=False,
                                  M_MessagesTypeID=dataType_query[0],
                                  M_FromUserID=sender_query[0],
                                  M_ToUserID=reciver_query[0],
                                  M_PostMessages=json.dumps(messages)
                                  )
      request.websocket.send(b'{"step":"5"}')
  # else:
    # messages = request.GET
    # print(messages)
    # return render(request, "text.html")


# 发送好友列表
@accept_websocket
def send_friend(request):
  # if request.is_websocket():
  #   for message in request.websocket:
  #     request.websocket.send(message)
  #     print(message)
  # else:
  #   message = request.GET
  #   print(message)
  #   return render(request, "test.html")
  pass

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


# 根据IP获取城市
def get_city(ip):
  url = "http://ip.tool.chinaz.com/?IP={}".format(ip)
  headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"}
  responses = requests.get(url, headers=headers)
  context = responses.content.decode("utf-8")
  city = re.findall(r'span class="Whwtdhalf w50-0">.*?省(\w+?)市.*?</span>', context,re.S)
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
  # 抓取当天气温(非实时)
  aim = re.findall('<input type="hidden" id="hidden_title" value=".*?\w{2}  (.*?)  (.*?)"',
                   response.text, re.S)
  print("今日气温：%s %s" % aim[0])
  return aim[0]


# 爬取新华网资讯
def get_news():
  news_list = []
  headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"}
  url = "http://www.xinhuanet.com/politics/"
  response = requests.get(url, headers=headers)
  text = response.content.decode('utf-8')
  # 初步过滤
  info = re.findall(r'<div class="wrap">.*?</a></div>', text,re.S)
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
