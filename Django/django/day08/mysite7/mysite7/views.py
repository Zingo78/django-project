import os
import time

from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.cache import cache_page
import csv
from upload_app.models import Content
from django.views.decorators.csrf import csrf_exempt


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


### day08
def test_upload(request):
    if request.method == 'GET':
        return render(request, 'test_upload.html')
    elif request.method == 'POST':
        title = request.POST['title']
        myfile = request.FILES['myfile']

        Content.objects.create(title = title, picture = myfile)

        return HttpResponse('--文件上传成功--')



# @csrf_exempt
# def upload_view(request):
#     if request.method == 'GET':
#         return render(request, 'test_upload.html')
#     elif request.method == 'POST':
#         a_file = request.FILES['myfile']
#         print('上传文件名是：', a_file.name)
#         filename = os.path.join(settings.MEDIA_ROOT,a_file.name)
#         with open(filename, 'wb') as f:
#             data = a_file.file.read()
#             f.write(data)
#         return HttpResponse('接受文件'+ a_file.name +'成功')










