from django.db import models

# Create your models here.
class User_user(models.Model):
    id=models.AutoField(primary_key=True)
    username=models.CharField("用户名",max_length=128,unique=True)
    password=models.CharField('密码',max_length=128)
    email=models.EmailField("邮箱")
    mobile_number=models.CharField("手机号码",max_length=128)
    login_time=models.DateTimeField("登录时间",auto_now=True)
    logout_time=models.DateTimeField("退出时间",auto_now=True)
    creat_time=models.DateTimeField("注册时间",auto_now_add=True)
    ip_address=models.CharField("IP地址",max_length=15)
    is_active=models.IntegerField("是否有效")



class User_info(models.Model):
    uid=models.AutoField(primary_key=True)
    nickname=models.CharField("昵称",max_length=128)
    sex=models.IntegerField("性别")
    age=models.IntegerField("年龄")
    profile_head=models.CharField("头像",max_length=255,null=True)
    profile=models.CharField("个性签名",max_length=255,null=True)
    user=models.OneToOneField(User_user)