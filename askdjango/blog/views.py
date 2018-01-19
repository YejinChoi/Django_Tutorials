import os
from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponse, JsonResponse
from django.conf import settings
from .models import Post
from django.http import Http404
from .forms import PostForm

#blog/views.py

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

    response =  render(request, 'blog/post_list.html',{
        'post_list' : qs,
        'q' : q,
    }) #템플릿을 통한 렌더링으로 response주는것이 좋다
    #HttpResponse 인스턴스인데, render를 통해서, 좀 더 쉽게 템플릿을 통한 렌더링
    return response

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


def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            return redirect(post) #get_absoulute_url 함수 구현했으므로 이렇게 사용 가능
            #post.get_absolute_url() => post.detail()로 이동
    else:
        form = PostForm()
    return render(request, 'blog/post_form.html', {'form' : form},)


def post_edit(request, id):
    post = get_object_or_404(Post, id=id)

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES,instance=post)
        if form.is_valid(): # 이때, 유효성 검사가 수행됨
            post = form.save()
            return redirect(post)

    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_form.html',
                  {'form' : form, })

