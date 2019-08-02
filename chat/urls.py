from django.conf.urls import url
from . import views

urlpatterns=[
  url(r"^index$",views.chat),
  # url(r"^index/get_weather$",views.ajax_weather),
]