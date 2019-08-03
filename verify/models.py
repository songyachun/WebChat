from django.db import models

class Province(models.Model):
    P_ID=models.AutoField(primary_key=True)
    P_name=models.CharField("省份名",max_length=30)


#城市表
class City(models.Model):
    C_ID=models.AutoField(primary_key=True)
    C_Name=models.CharField("城市名",max_length=30)
    #外键：关联省份表
    P_ProcvinceID=models.ForeignKey(Province,related_name="所属省份",on_delete=models.CASCADE)


# Create your models here.
class User(models.Model):
    # id=models.AutoField(primary_key=True)
    username=models.CharField("用户名",max_length=128,unique=True)
    password=models.CharField('密码',max_length=128)
    email=models.EmailField("邮箱")
    mobile_number=models.CharField("手机号码",max_length=128)
    login_time=models.DateTimeField("登录时间",auto_now=True)
    logout_time=models.DateTimeField("退出时间",auto_now=True)
    creat_time=models.DateTimeField("注册时间",auto_now_add=True)
    ip_address=models.CharField("IP地址",max_length=15)
    is_active=models.IntegerField("是否有效",default="1")
    # 外键：“好友”,关联自身
    friends = models.ManyToManyField('self', related_name='my_friends', blank=True)


class UserInfo(models.Model):
    uid=models.AutoField(primary_key=True)
    nickname=models.CharField("昵称",max_length=128)
    sex=models.IntegerField("性别")
    age=models.IntegerField("年龄")
    brithday=models.CharField("生日",max_length=100,null=True)
    profile_head = models.ImageField("头像", blank=True, null=True, upload_to="upload")
    profile=models.CharField("个性签名",max_length=255,null=True)
    user=models.OneToOneField(User)
    # 外键：关联省份表
    province_id = models.ForeignKey(Province, related_name="省份ID", default="")
    # 外键；关联城市表
    city_id = models.ForeignKey(City, related_name="省份ID", default="")


#消息类型
class MessagesType(models.Model):
    MT_ID=models.AutoField(primary_key=True)
    MT_Name=models.CharField("类型名称",max_length=20)

#聊天记录表
class Messages(models.Model):
    M_ID=models.AutoField(primary_key=True)
    M_PostMessages=models.TextField("消息内容")
    M_status=models.BooleanField("接收状态")
    M_time=models.DateTimeField("发送时间",auto_now_add=True)
    #外键：关联消息类型表
    M_MessagesTypeID=models.ForeignKey(MessagesType,related_name='消息类型ID')
    M_FromUserID=models.OneToOneField(User,related_name="发送者ID")
    M_ToUserID=models.OneToOneField(User,related_name="接收者ID")


#用户群表
class User_Group(models.Model):
    UG_ID=models.AutoField(primary_key=True)
    UG_Name=models.CharField("群名称",max_length=30)
    UG_CreatTime=models.DateTimeField("创建时间",auto_now_add=True)
    #外键：关联用户表
    UG_AdminId=models.ForeignKey(User,related_name="群主ID")
    UG_ICon=models.CharField("群图标",max_length=30)
    UG_Notice=models.CharField("群公告",max_length=200)
    UG_Intro=models.CharField("群简介",max_length=200)

#群用户关联表
class User_GroupsToUser(models.Model):
    UG_ID=models.AutoField(primary_key=True)
    #外键：关联用户表
    UG_UserID=models.ManyToManyField(User,related_name="群用户ID")
    #外键：关联用户群表
    UG_GroupID=models.OneToOneField(User_Group)
    UG_CreateTime=models.DateTimeField("发送时间",auto_now=True)

#群消息内容表
class User_GroupsMSGContent(models.Model):
    GM_ID=models.IntegerField(primary_key=True)
    GM_Content=models.TextField("消息内容")
    GM_FromID=models.IntegerField("发送者ID")
    GM_CreateTime=models.DateTimeField("发送时间",auto_now_add=True)

#群消息关联表
class User_GroupsMSGToUser(models.Model):
    GM_ID=models.AutoField(primary_key= True)
    GM_UserID=models.IntegerField("接收者ID")
    #外键：关联群消息内容表
    GM_GroupMessageID=models.OneToOneField(User_GroupsMSGContent)
    GM_State=models.BooleanField("接收状态")
    GM_CreateTime=models.DateTimeField("发送时间",auto_now=True)
