import os
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.conf import settings


# 함수 기반 뷰의 4가지 응답
# Create your views here.
# def mysum(request,x,y=0):
    #request : HttpRequest
    #return HttpResponse(int(x)+int(y))


def mysum(request,numbers):
    #request : HttpRequest
    #result = sum(map(int, numbers.split("/")))
    result = sum(map(lambda s : int(s or 0), numbers.split("/")))
    return HttpResponse(result)


def hello(request, name, age):
    return HttpResponse('안녕하세요. {}. {} 살 이시네요.'.format(name,age))


# HTTPResponse로 응답
def post_list1(request):
    name = '공유'
    return HttpResponse('''
        <h1>AskDjango</h1>
        <p>{name}</p>
    '''.format(name=name))


# 템플릿을 통한 응답
def post_list2(request):
    name = 'Yejin'
    return render(request,'blog/post_list2.html', {'name':name})


# json 통한 응답
def post_list3(request):
    return JsonResponse({
        'message' : 'Python',
        'items' : ['dd','sdfsd','dsffwefwfsd']
    },json_dumps_params={'ensure_ascii':False})


# 파일 다운로드 응답
def excel_download(request):
    #filePath = '/home/yejinchoi/Downloads/ie_data.xls'
    filePath = os.path.join(settings.BASE_DIR, 'ie_data.xls')
    filename = os.path.basename(filePath)
    with open(filePath,'rb') as f:
        response  = HttpResponse(f, content_type = 'application/vnd.ms-excel') #text-html
        #필요한 응답헤더 세팅
        response['Content-Disposition'] = 'attachment;filename="{}"'.format(filename)
        return response
