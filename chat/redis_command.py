import redis
import time, random
import multiprocessing
r = redis.Redis(host="localhost",
                port=6379,
                db=0,
                password="123456")

r.mset({"username":"news","password":"1234563"})
print(r.mget("username","password"))

def push():
  # 生成url地址
  for page in range(0, 10):
    url = "http://app.mi.com/category/2#page=%s" % str(page)
    r.lpush("spider::urls", url)
    time.sleep(random.randint(1, 3))

def pop():
  # 消费url地址
  while True:
    url=r.blpop("spider::urls",3)
    # print(url[1])
    if url:
      print("正在抓取%s"%url[1].decode())
    else:
      print("抓取结束")
      break

p1=multiprocessing.Process(target=push)
p2=multiprocessing.Process(target=pop)
p1.start()
p2.start()
p1.join()
p2.join()