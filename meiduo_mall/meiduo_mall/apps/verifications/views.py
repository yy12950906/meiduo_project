from django.shortcuts import render
from django.views import View
from meiduo_mall.libs.captcha.captcha import captcha
from django_redis import get_redis_connection
from django import http
from . import constants




class ImageCodeView(View):
    """图形验证码"""

    def get(self, request, uuid):
        # 生成图形验证码
        # name唯一标识，image_code_text图形验证码的字符，image_bytes图形验证码bytes
        name,image_code_text,image_bytes = captcha.generate_captcha()

        # 创建redis连接对象
        redis_conn = get_redis_connection('verify_code')
        # 将图形验证码的字符存储到redis中，用uuid作为key
        redis_conn.setex(uuid, constants.IMAGE_CODE_REDIS_EXPIRES, image_code_text)
        # 响应 把生成好的图片验证码bytes数据作为响应体响应给前端
        return http.HttpResponse(image_bytes, content_type='image/jpg')

