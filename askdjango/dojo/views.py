import os
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse,JsonResponse
from django.conf import settings
from .forms import PostForm
from .models import Post

# Create your views here.
#함수 기반 뷰의 4가지 응답

#def my_sum(request,x,y):
#    return HttpResponse(int(x)+int(y))

def my_sum(requset, numbers):
    result = sum(map(int, numbers.split("/")))
    return HttpResponse(result)

def hello(request,name, age):
    return HttpResponse('안녕하세요. HelloWorld {}님. {}세'.format(name,age))


#1. HttpResponse로 응답
def post_list1(request):
    name = 'Smilegate'
    return HttpResponse('''
        <h1>Django-dojo-views.py</h1>
        <p><strong>{name}</strong></p>
    '''.format(name=name))


#2. 템플릿을 통한 응답
def post_list2(request):
    name='smileGateSerDevCamp'
    return render(request,'dojo/post_list.html',{'name':name})


#3. JsonResponse로 응답
def post_list3(request):
    return JsonResponse({
        'messages' : 'Python3-Django-Tutorial',
        'items' : ['Python3.6.3','pycharm','community']
    }, json_dumps_params={'ensure_ascii':False})

#4. 파일 다운로드 응답
def excel_download(request):
    filePath = os.path.join(settings.BASE_DIR,'ie_data.xls')
    filename = os.path.basename(filePath)
    with open (filePath,'rb') as f:
        response = HttpResponse(f, content_type = 'application/vnd.ms-excel')
        # 필요한 응답헤더 세팅
        response['Content-Disposition'] = 'attachment;filename="{}"'.format(filename)
        return response


def post_new(request):
    if request.method == 'POST': # 유저가 데이터 보내는 경우이므로
        form = PostForm(request.POST, request.FILES) # file이 없으면 request.FILES 없어도 된다
        if form.is_valid():
            # 방법5)dojo/forms.py에 구현
            post = form.save(commit=False)
            post.ip = request.META['REMOTE_ADDR']
            post.save()
            return redirect('/dojo/')
            # DB저장 방법1)
            # post = Post()
            # post.title = form.cleaned_data['title']
            # post.content = form.cleaned_data['content']
            # post.save()

            # 방법2)
            # post = Post(title=form.cleaned_data['title'], content=form.cleaned_data['content'])
            # post.save()

            # 방법3)
            # post = Post.objects.create(title=form.cleaned_data['title'], content=form.cleaned_data['content'])
            # post.save()

            # 방법4)
            # post = Post.objects.create(**form.cleaned_data)


            #print(form.cleaned_data) #user의 data를 사전형태로 제공받을 수 있음
            #return redirect('/dojo/') #namespace : name
        #else: #검증에 실패하면, form.errors와 form.각필드.errors에 오류 정보를 저장
            #form.errors
    else:
        form = PostForm()
    return render(request, 'dojo/post_form.html', {'form' : form},)


def post_edit(request,id):
    post = get_object_or_404(Post, id=id)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES,instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.ip = request.META['REMOTE_ADDR']
            post.save()
            return redirect('/dojo/')
        else:
            form.errors
    else:
        form = PostForm(instance=post)

    return render(request, 'dojo/post_form.html',
                  {'form' :  form},)