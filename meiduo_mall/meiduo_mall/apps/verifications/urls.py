from django.conf.urls import url
from . import views


urlpatterns = [
    # 获取图形验证码
    url(r'^image_codes/(?P<uuid>[\w-]+)/$', views.ImageCodeView.as_view()),
]