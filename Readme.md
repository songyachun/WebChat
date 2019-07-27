# AID1904中期项目--多人即时聊天

## 功能

1. 用户的登录和注册
2. 并发：支持连接处理多个用户请求
3. 即时聊天
4. 离线接收消息，历史记录
5. 好友列表
6. 好友在线状态
7. 群聊功能
8. 查询天气，笑话

## 技术分析

1. Web后端框架选择：Django

2. 全双工通讯：由于是即时聊天，需要服务器主动向浏览器推送数据，http通讯协议无法满足

   1. 引用WebSocket，全双工通讯的协议。
   2. Django使用Channels实现WebSocket

   - https://www.cnblogs.com/37Y37/p/10721465.html

3. 并发：多用户同时操作  主要为IO操作  
   1. 多线程/多进程并发：占用较多的资源
      1. fork多进程
   2. IO多路复用：I/O多路复用是在单一进程的上下文中的，因此每个逻辑流程都能访问该进程的全部地址空间，所以开销比多进程低得多；缺点是编程复杂度高。
      1. select方式，支持多平台，逻辑简单，支持最大并发数量（1024），相对epoll效率较低
      2. poll方式，
      3. epoll方式，

4. 数据存储：用户信息存储，用户名和密码  历史记录
   1. 数据库存储：查询效率高，方便程序调用，做自动化处理
      1. 数据库选择：mysql
   2. 实现方式：通过Django的Model模型层，对数据库进行相对的增删改查（CURD）
   
5. 界面：使用html文件在web浏览器上呈现

## 结构设计

1. 基于Django框架的设计
2. 由于Django是B/S架构，使用浏览器作为客户端
   1. 通讯模块
      1. 与客户端通讯，接收客户端的请求，将响应发送给客户端
      2. 与数据库通讯，数据的增删改查
   2. 并发处理模块
      1. 同时处理多个客户端请求
   3. 逻辑处理模块
      1. 处理客户请求，组织响应内容
3. 数据库操作类（查询，增加，修改）
   1. 数据库名称：wechat_db

## 功能模块设计

### 注册：

#### 功能

1. 确保用户名，手机号唯一
2. 用户名和密码约束

   - 用户名（字段约束）--由2-10位字母、数字、下划线或中文组成，以字母或中文开头
   - 昵称（可以相同）
   - 邮箱（字段验证）-- 符合邮箱格式
   - 密码（长度限制，字段约束）-- 
     - 由6-12位字母、数字组成
     - 不能全部是数字
     - 不能全部是字母
     - 必须是数字或字母
3. 密码加密
   - 密码隐式存储在数据库中，可选择加盐加密方法
4. 用户状态验证
   - 登入记住用户名功能
   - 禁止用户未登入直接进入聊天界面
5. 短信验证
   - 手机短信验证
#### 实现

1. 注册页面路径：/verify/signup
2. 需要post的数据名：username，password...
3. 服务端：
   1. 接收，判断用户名是否已经存在，存在返回”用户名已经存在“，反之返回注册成功，并进入聊天界面
   2. 存储注册成功的用户，密码使用加盐加密
   3. session验证：
      - 验证用户是不是一个合法用户
      - 在当前用户的session上记录当前用户名的名称和id
        - request.session["user"]={"user":"news","id":1}
      - 没有登陆的用户 session["user"]不存在
      - 退出登陆时，删除session["user"]

### 登录

1. 路径：/verify/signin
2. 记住上一次登入的用户名
   1. 使用cookie存储用户名

### 并发

- 使用 nginx + uwsgi 为 django 提供高并发 web 服务


### 第三周任务

- 登入界面忘记密码
- 修改用户个人信息
  - 上传头像
  - 修改密码、邮箱、电话号码、昵称、性别
- 实时搜索天气，新闻头条
    - 根据客户端访问的IP，获取所在城市，查询天气，显示在聊天主界面
    - 爬取新华网的五条头条新闻，显示在聊天主界面
        - 图片、文章链接、标题
- 友情链接
- 上传下载文件
- 添加好友，显示好友列表
### 实时搜索天气
- 根据用户个人信息所在的城市，在中国天气网爬取实时的天气

### 即时聊天

  

#### 协议设计

1. 请求格式


-----------------------------------

# 2019.7.22 修改登录界面
## 登录界面 --> login.html
1. 添加忘记密码界面展示
2. 修改提示错误样式

# 2019.7.23 增加忘记密码功能
## 忘记密码功能
1.  忘记密码界面 --> password_reset.html
2.  修改密码界面 --> password_reset2.html

## 修改注册界面的获取验证码界面
1. 注册界面 --> signup.html
2. 添加输入验证码文本框 name="veri_code"
