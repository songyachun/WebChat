from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
import pymysql

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
    # username=request.COOKIES.get("old_user","")
    ip=request.META['REMOTE_ADDR']
    print(ip)
    weather=get_weather(ip)
    news_list=get_news()
    return render(request, "main.html", locals())


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
  sql = '''select code from city_code where city="%s";''' %(city)
  cursor.execute(sql)
  # 查询结果
  city_code=cursor.fetchone()
  if not city_code:
    return 101280601
  conn.close()
  return city_code[0]

def get_city(ip):
  url="http://ip.tool.chinaz.com/?IP={}".format(ip)
  headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"}
  responses=requests.get(url,headers=headers)
  context=responses.content.decode("utf-8")
  city=re.findall(r'span class="Whwtdhalf w50-0">.*?省(\w+?)市.*?</span>',context)
  print (city)
  return city[0]

# 根据客户端ip获取天气
def get_weather(ip):
  try:
    city=get_city(ip)
  except:
    city="深圳"
  url= "http://www.weather.com.cn/weather1d/{}.shtml".format(get_city_code(city))
  response = requests.get(url)
  response.encoding = 'utf-8'
  # 抓取当天气温（非实时）
  aim = re.findall('<input type="hidden" id="hidden_title" value=".*?\w{2}  (.*?)  (.*?)"',
                   response.text, re.S)
  print("今日气温：%s %s" % aim[0])
  return aim[0]

def get_news():
  news_list=[]
  headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"}
  url = "http://www.xinhuanet.com/politics/"
  response = requests.get(url, headers=headers)
  text = response.content.decode('utf-8')
  # 初步过滤
  info = re.findall(r'<div class="wrap">.*?</a></div>', text)
  # 获得五条新闻
  n=0
  for i in info:
    url_img = re.findall(r'data-original=(.*?) /> ', i)
    url_html = re.findall(r'<a href="(.*?)" target="_blank">', i)
    title = re.findall(r'_blank">(.*?)</a></div>', i)
    news_list.append(url_img+url_html+title)
    n+=1
    if n >4:
      return news_list


if __name__ == "__main__":
    get_weather("深圳")
    print(get_city_code("深圳"))
    print(get_news())
    get_city("118.212.211.13")
# <p class="tem on">最高气温: 33℃ , 最低气温: 26℃</p>

