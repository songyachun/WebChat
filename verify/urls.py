from django.conf.urls import url
from . import views

urlpatterns=[
  # 注册
  url(r"^signup",views.register_verify),
  # 登录
  url(r"^signin",views.sign_in),
  url(r'^personal_set',views.personal_set),
]