from django.conf.urls import url
from . import views

urlpatterns=[
  url(r"^index$",views.chat),
  # url(r"^index/get_weather$",views.ajax_weather),
  # 好友请求
  url(r"friend_id$",views.add_friend),
  # 推送好友列表
  url(r"friend_list$",views.send_friend),
]