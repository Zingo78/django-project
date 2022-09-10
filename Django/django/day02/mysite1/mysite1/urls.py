"""mysite1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # path('', views.home),

    # # http://127.0.0.1:8000/page/2003
    path('page/2003', views.page_2003_view),

    # #http://127.0.0.1:8000/
    path('', views.index_view),

    # # http://127.0.0.1:8000/page/1
    path('page/1', views.page1_view),

    # # http://127.0.0.1:8000/page/2
    path('page/2', views.page2_view),

    # # http://127.0.0.1:8000/page/3-100
    path('page/<int:pg>', views.pagen_view),

    # # http://127.0.0.1:8000/整数/操作符/整数
    re_path(r'^(?P<x>\d{1,2})/(?P<op>\w+)/(?P<y>\d{1,2})$', views.cal2_view),

    # # http://127.0.0.1:8000/整数/操作符/整数
    path('<int:n>/<str:op>/<int:m>', views.cal_view),

    # # http://127.0.0.1:8000/birthday/年4/月2/日2
    re_path(r'^birthday/(?P<y>\d{4})/(?P<m>\d{1,2})/(?P<d>\d{1,2})$', views.birthday_view),
    # # http://127.0.0.1:8000/birthday/月2/日2/年4
    re_path(r'^birthday/(?P<m>\d{1,2})/(?P<d>\d{1,2})/(?P<y>\d{4})$', views.birthday_view),


    ###day02###
    path('test_request', views.test_request),
    path('test_get_post', views.test_get_post),
    path('test_html', views.test_html),
    path('test_html_param', views.test_html_param),
    path('test_if_for', views.test_if_for),

    path('mycal', views.mycal),

    path('base_index', views.base_view,name = 'base_index'),
    path('music_index', views.music_view),
    path('sport_index', views.sport_view),
    # http://127.0.0.1:8000/test/url
    path('test/url', views.test_url),
    path('test_urls_result/<int:age>', views.test_url_result, name = 'tr'),


]
