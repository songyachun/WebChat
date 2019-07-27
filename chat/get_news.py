import requests
import re


def get_news():
  headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"}
  url = "http://www.xinhuanet.com/politics/"
  response = requests.get(url, headers=headers)
  text = response.content.decode('utf-8')
  # 初步过滤
  info = re.findall(r'<div class="wrap">.*?</a></div>', text)
  # 获得我们要的信息
  for i in info:
    url_img = re.findall(r'data-original=(.*?) /> ', i)
    url_html = re.findall(r'<a href="(.*?)" target="_blank">', i)
    title = re.findall(r'_blank">(.*?)</a></div>', i)
    print(url_img)
    print(url_html)
    print(title)


get_news()
