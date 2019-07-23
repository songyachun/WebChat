from django.conf.urls import url
from . import views

urlpatterns=[
  # 注册
  url(r"^signup",views.register_verify),
  # 登录
  url(r"^signin",views.sign_in),
  # 忘记密码
  url(r'^pwd_reset/$',views.pwd_reset),
  url(r'^pwd_reset2/$',views.pwd_reset2),
]