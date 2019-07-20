from django.db import models


# Create your models here.
class UserInfo(models.Model):
  username = models.CharField("用户名", max_length=20, null=False)
  password = models.CharField("密码", max_length=100, null=False)
  email = models.CharField("邮箱", max_length=30, null=True)

  def __str__(self):
    return "用户名：%s 邮箱：%s" % (self.username, self.email)
  # status = models.IntegerField(max_length=5)
  # auth = models.IntegerField(max_length=5)
  # loginTime = models.DateTimeField()
  # createTime = models.DateTimeField()
  # logoutTime = models.DateTimeField()
