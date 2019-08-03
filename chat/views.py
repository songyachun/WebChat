import json

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


# 函数装饰器，检查用户是否登入，没有登入跳转登入页面
from verify.models import User, Messages, MessagesType


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
    email_link = email_address_dict[email_sign[0]]

    # 爬虫相关设置
    ip = request.META['REMOTE_ADDR']
    # print(ip)
    weather = get_weather(ip)
    news_list = get_news()
    return render(request, "main.html", locals())

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
  return  HttpResponse(resText)

def send_message(request):
  if request.method == "GET":
    return render(request, "test.html")


# @require_websocket
# def echo_once(request):
#   message = request.websocket.wait()
#   request.websocket.send(message)
#   # 监听接收客户端发送的消息 或者 客户端断开连接
#   if request.is_websocket():
#     print(00000)
#     message = request.websocket.wait()
#   # for message in request.websocket:
#   if message:
#     print(11111)
#     request.websocket.send('大鱼'.encode())  # 发送给前段的数据
#     time.sleep(2)
#   else:
#     print(232222222222)
#     request.websocket.colse()

# 处理好友请求
@accept_websocket
def add_friend(request):
  if request.is_websocket():
    for messages in request.websocket:
      messages=json.loads(messages)
      # 获取add_friend的步骤
      step=messages.get("step")
      sender=messages.get("sender")
      sender_query=User.objects.filter(username=sender)
      # 判断发送者和接收者是否存在
      if not sender_query:
        request.websocket.send(b'{"code":101,"error":"The sender is not existed"}')
        continue
      reciver=messages.get("reciver")
      reciver_query = User.objects.filter(username=reciver)
      if not reciver_query:
        request.websocket.send(b'{"code":102,"error":"The reciver is not existed"}')
        continue
      type = messages.get("type")
      print(type)
      type_query = MessagesType.objects.filter(MT_Name=str(type))
      if not type_query:
        request.websocket.send(b'{"code":102,"error":"The type is not existed")}')
        continue
      # 接收申请请求
      if step=="0":
        print(sender_query,reciver_query,type_query)
        # 添加消息
        Messages.objects.create(M_status="0",
                                M_MessagesTypeID=type_query[0],
                                M_FromUserID=sender_query[0],
                                M_ToUserID=reciver_query[0]
                                )
      # 发送申请响应
      elif step==1:
        pass
      # 接收应答请求
      elif step==2:
        pass
      # 发送应达响应
      elif step==3:
        pass
      print(messages)
      request.websocket.send(b'{"title":1}')
  else:
    messages = request.GET
    print(messages)
    return render(request, "test.html")

# 发送好友列表
@accept_websocket
def send_friend(request):
  if request.is_websocket():
    for message in request.websocket:
      request.websocket.send(message)
      print(message)
  else:
    message = request.GET
    print(message)
    return render(request, "test.html")

# 查询数据库,返回城市对应的编码
def get_city_code(city):
  # 连接数据库,charset参数必填
  conn = pymysql.connect(host='localhost',
                         port=3306,
                         user='root',
                         password='123456',
                         database='webchat',
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
