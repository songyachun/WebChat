from django.conf.urls import url
from . import views

urlpatterns = [
    url(r"^index$", views.chat),
    url(r'^personal_set$', views.mod_user_info),
    url(r'^change_password$',views.mod_pwd),
    url(r'^inter_layout$',views.inter_layout),
    url(r'^feedback$',views.feedback),
]
