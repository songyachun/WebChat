"""
  在中国天气网抓取所有城市和城市对应的编码
"""

import re
import requests
import pymysql

# 定制请求头
headers = {
  'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}
# 用列表存储爬取下来编码和城市名
cites_codes = []


# 爬取解析一个网页的函数
def parse_url(url):
  response = requests.get(url, headers=headers)
  text = response.content.decode('utf-8')
  # 先滤去后面六个，只留下第一个
  info = re.findall(
    r'<div class="conMidtab">.*?<div class="conMidtab" style="display:none;">', text, re.DOTALL)[0]
  # 获得我们要的信息
  infos = re.findall(
    r'<td width="83" height="23".*?<a .*?weather/(.*?)\.s.*?>(.*?)</a>', info, re.DOTALL)
  # 获取的信息遍历存入列表
  for i in infos:
    city_code = [i[1], i[0]]
    cites_codes.append(city_code)


# 存储到数据库函数
def store_2_mysql():
  # 连接数据库,charset参数必填
  conn = pymysql.connect(host='176.140.10.214',
                         port=3306,
                         user='root',
                         password='123456',
                         database='webchat_db',
                         charset="utf8")
  cursor = conn.cursor()
  #遍历列表存入数据库
  for i in cites_codes:
    sql = '''insert into city_code(city,code) values('%s','%s');''' %(i[0], i[1])
    # sql = '''insert into city_code(city,code) values('上海','12331');'''
    cursor.execute(sql)
  # cursor.execute("insert into city_code(city,code) values('上海','12331');")
  # 提交
  conn.commit()
  conn.close()


# 主函数遍历全部八个地区
def main():
  base_url = 'http://www.weather.com.cn/textFC/{}.shtml'
  cites = ['hb', 'db', 'hd', 'hz', 'hn', 'xb', 'xn', 'gat']
  # 获得每个地区的url
  for i in cites:
    url = base_url.format(i)
    # 开始爬取一个地区的信息
    parse_url(url)
  # 存储到数据库中
  store_2_mysql()
  # print(cites_codes)


if __name__ == '__main__':
  main()
