from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from django.conf import settings
from alipay import AliPay
import time


app_private_key_string = open(settings.ALIPAY_KEY_DIRS + 'app_private_key.pem').read()
alipay_public_key_string = open(settings.ALIPAY_KEY_DIRS + 'alipay_public_key.pem').read()


class MyAliPay(View):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.alipay = AliPay(
            appid=settings.ALIPAY_APPID,
            app_private_key_string=app_private_key_string,
            alipay_public_key_string=alipay_public_key_string,
            app_notify_url=None,
            sign_type="RSA2",
            debug=True
        )

    def get_trade_url(self, order_id, amount):

        order_string = self.alipay.api_alipay_trade_page_pay(
            subject=order_id,
            out_trade_no=order_id,
            total_amount=amount,
            #支付完毕之后，将用户跳转至哪个页面
            return_url=settings.ALIPAY_RETURN_URL,
            notify_url=settings.ALIPAY_NOTIFY_URL
        )

        return "https://openapi.alipaydev.com/gateway.do?" + order_string


class OrderView(MyAliPay):
    def get(self, request):
        return render(request, 'alipay.html')
    def post(self, request):
        # 返回支付地址
        #接收到文章id后，生成订单 订单状态 代付款 已付款 付款失败
        order_id = '%sGXN' %(int(time.time()))
        pay_url = self.get_trade_url(order_id, 999)

        return JsonResponse({"pay_url":pay_url})
        # return JsonResponse({"pay_url":'http://www.baidu.com'})