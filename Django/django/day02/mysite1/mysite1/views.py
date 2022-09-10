from django.http import HttpResponse, HttpResponseRedirect

POST_FORM = '''
<form method='post' action='/test_get_post'>
    用户名:<input type='text' name='uname'>
    <input type='submit' value='提交'>
</form >
'''



def home(request):
    return HttpResponse('ok')


def page_2003_view(request):

    html = "<h1>这是第一个页面</h1>"
    return HttpResponse(html)

def index_view(request):
    html = '这是我的首页'
    return HttpResponse(html)

def page1_view(request):
    html = '这是编号为1的网页'
    return HttpResponse(html)

def page2_view(request):
    html = '这是编号为2的网页'
    return HttpResponse(html)

def pagen_view(request, pg):

    html = '这是编号为%s的网页'%(pg)
    return HttpResponse(html)

def cal_view(reeuest, n, op, m):

    if op not in ['add', 'sub', 'mul']:
        return HttpResponse('Your op is wrong')

    result = 0
    if op == 'add':
        result = n+m
    elif op == 'sub':
        result = n-m
    elif op == 'mul':
        result = n*m

    html = '结果:%s'%(result)
    return HttpResponse(html)


def cal2_view(reeuest, x, op, y):

    html = 'x:%s op:%s y:%s'%(x, op, y)
    return HttpResponse(html)

def birthday_view(request, y, m, d):

    html = '生日为%s年%s月%s日'%(y,m,d)
    return HttpResponse(html)


def test_request(request):

    print('path info is', request.path_info)
    print('method is', request.method)
    print('querystring is', request.GET)
    print('full path is', request.get_full_path())

    # return HttpResponse('test request ok')
    return HttpResponseRedirect('/page/1cc')



def test_get_post(request):

    if request.method == 'GET':
        print(request.GET)
        print(request.GET['a'])
        print(request.GET.getlist('a'))
        print(request.GET.get('c', 'no c'))
        return HttpResponse(POST_FORM)

    elif request.method == 'POST':
        # 处理用户提交数据
        print('uname is',request.POST['uname'])
        return HttpResponse('post is ok')
    else:
        pass

    return HttpResponse('--test get post is ok--')


def test_html(request):

    # # 方案一
    # from django.template import loader
    # t = loader.get_template('test_html.html')
    # html = t.render()
    # return HttpResponse(html)


    #方案二
    from django.shortcuts import render
    dic = {'username':'guoxiaonao', 'age':18}
    return render(request, 'test_html.html', dic)


from django.shortcuts import render
def test_html_param(request):
    dic={}
    dic['int']=88
    dic['str']='guoxiaonao'
    dic['lst']=['Tom','Jack', 'Lily']
    dic['dict'] = {'a':9, 'b':8}
    dic['func'] = say_hi
    dic['class_obj'] = Dog()
    dic['script'] = '<script>alert(1111)</script>'

    return render(request, 'test_html_param.html', dic)

def say_hi():
    return 'hahaha'
class Dog:
    def say(self):
        return 'wangwang'



def test_if_for(request):
    dic = {}
    dic['x'] = 10
    dic['lst'] = ['Tom', 'Jack', 'Lily']
    return render(request, 'test_if_for.html', dic)


def mycal(request):
    if request.method == 'GET':
        return render(request, 'mycal.html')
    elif request.method == 'POST':
        # 处理计算
        x = int(request.POST['x'])
        y = int(request.POST['y'])
        op = request.POST['op']

        result = 0
        if op == 'add':
            result = x + y
        elif op == 'sub':
            result = x - y
        elif op == 'mul':
            result = x * y
        elif op == 'div':
            result = x / y

        # dic = {'x':x, 'y':y, 'op':op}
        return render(request, 'mycal.html', locals())

def base_view(request):
    lst = ['Tom', 'Jack']
    return render(request, 'base.html', locals())

def music_view(request):
    return render(request, 'music.html')


def sport_view(request):
    return render(request, 'sport.html')



def test_url(request):
    return render(request, 'test_url.html')


def test_url_result(request, age):


    #302跳转
    from django.urls import reverse
    url = reverse('base_index')
    return HttpResponseRedirect(url)


    # return HttpResponse('---test url res is ok')
























