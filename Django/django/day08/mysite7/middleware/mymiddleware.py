from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin
import re
import traceback
from django.core import mail
from django.conf import settings


class MyMW(MiddlewareMixin):

    def process_request(self, request):

        print('MyMW process_request do ---')

    def process_view(self, request, callback, callback_args, callback_kwargs):
        print('MyMW process_views do ---')

    def process_response(self, reuqest, response):

        print('MyMW process_response do ---')
        return response



class MyMW2(MiddlewareMixin):

    def process_request(self, request):

        print('MyMW2 process_request do ---')

    def process_view(self, request, callback, callback_args, callback_kwargs):
        print('MyMW2 process_views do ---')

    def process_response(self, reuqest, response):

        print('MyMW2 process_response do ---')
        return response



class VisitLimit(MiddlewareMixin):


    visit_times = {}

    def process_request(self, request):
        ip_address = request.META['REMOTE_ADDR']
        path_url = request.path_info
        if not re.match('^/test', path_url):
            return
        times = self.visit_times.get(ip_address,0)
        print('ip', ip_address, '已经访问', times)
        self.visit_times[ip_address] = times + 1
        if times < 5:
            return
        return HttpResponse('您已经访问过' + str(times) + '次,访问被禁止')



class ExceptionMW(MiddlewareMixin):

    def process_exception(self, reqeust, exception):
        print(exception)
        print(traceback.format_exc())

        mail.send_mail(subject='mysite7报错了~', message=traceback.format_exc(), from_email='990284734@qq.com', recipient_list=settings.EX_EMAIL)


        return HttpResponse('---对不起 当前网页有点忙')





















