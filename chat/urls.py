from django.conf.urls import url
from . import views

urlpatterns=[
  url(r"^index$",views.chat),
  url(r'^get_weather',views.city_weather)
]