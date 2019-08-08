from django.conf.urls import url
from . import views

urlpatterns=[
  url(r"^index$",views.chat),
  # url(r"^index/get_weather$",views.ajax_weather),
  # 好友请求
  url(r"friend_id$",views.add_friend),
  # 推送好友列表
  url(r"friend_list$",views.send_friend),
  # 刷新天气
  url(r'^get_weather',views.city_weather),
  # 修改个人信息
 url(r'^personal_set$', views.mod_user_info),

  # 修改密码
  url(r'^change_password$', views.mod_pwd),
  # 上传头像
  url(r'^personal_set1$',views.upload_avatar),

  # ...
  url(r'^inter_layout$', views.inter_layout),
  url(r'^feedback$', views.feedback),
]
