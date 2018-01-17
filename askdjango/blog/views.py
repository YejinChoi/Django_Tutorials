import os
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.conf import settings
from .models import Post
from django.http import Http404


# 함수 기반 뷰의 4가지 응답
# Create your views here.
# def mysum(request,x,y=0):
    #request : HttpRequest
    #return HttpResponse(int(x)+int(y))

def post_list(request):
    qs = Post.objects.all()

    q = request.GET.get('q','')
    if q:
        qs = qs.filter(title__icontains=q) #q가 포함되어있는 queryset만 가져옴

    return render(request, 'blog/post_list.html',{
        'post_list' : qs,
        'q' : q,
    })


def mysum(request,numbers):
    #request : HttpRequest
    #result = sum(map(int, numbers.split("/")))
    result = sum(map(lambda s : int(s or 0), numbers.split("/")))
    return HttpResponse(result)


def hello(request, name, age):
    return HttpResponse('안녕하세요. {}. {} 살 이시네요.'.format(name,age))


# HTTPResponse로 응답 (200응답)
def post_list1(request):
    name = '공유'
    return HttpResponse('''
        <h1>AskDjango</h1>
        <p>{name}</p>
    '''.format(name=name))


# 템플릿을 통한 응답 (200응답)
def post_list2(request):
    name = 'Yejin'
    return render(request,'blog/post_list2.html', {'name':name})


# json 통한 응답 (200응답)
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


def post_detail(request, id):
    #try:
    #   post = Post.objects.get(id = id)
    #except (Post.DoesNotExist, Post.MultipleObjectsReturned):
    #    raise Http404

    post = get_object_or_404(Post, id=id) # try-except와 동일 - 이게 더 훨씬 간편
    return render(request, 'blog/post_detail.html',{
        'post' : post,
    })

