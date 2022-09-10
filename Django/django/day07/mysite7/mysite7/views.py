import time

from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.cache import cache_page
import csv

@cache_page(15)
def test_cache(request):
    t = time.time()

    return HttpResponse('t is %s'%(t))


def test_mw(request):
    print('---test_mw view in---')
    return HttpResponse('---test_mw---')



def test_csrf(request):

    if request.method == 'GET':
        return render(request, 'test_csrf.html')
    elif request.method == 'POST':
        return HttpResponse('---test post is ok---')


def test_page(request):
    #/test_page/4
    #/test_page?page=1
    page_num = request.GET.get('page', 1)
    all_data = ['a','b','c','d','e']
    #初始化paginator
    paginator = Paginator(all_data, 2)
    #初始化 具体页码的page对象
    c_page = paginator.page(int(page_num))
    return render(request,'test_page.html',locals())


def test_csv(reequest):

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment;filename="test.csv"'
    all_data = ['a','b', 'c','d']

    writer = csv.writer(response)
    writer.writerow(all_data)
    return response


def make_page_csv(request):
    page_num = request.GET.get('page', 1)
    all_data = ['a', 'b', 'c', 'd', 'e']
    # 初始化paginator
    paginator = Paginator(all_data, 2)
    # 初始化 具体页码的page对象
    c_page = paginator.page(int(page_num))

    response = HttpResponse(content_type='test/csv')
    response['Content-Disposition'] = 'attachment;filename="page-%s.csv"'%(page_num)
    writer = csv.writer(response)
    for b in c_page:
        writer.writerow([b])
    return response












