import os
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse,JsonResponse
from django.conf import settings
from .forms import PostForm
from .models import Post
from django.contrib import messages
from django.views.generic import DetailView

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
    post = get_object_or_404(Post, id=id) #인스턴스 획득
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

    return render(request, 'dojo/post_form.html',{
        'form' :  form,
    })

"""
# CBV 샘플- STEP 1. 함수 기반 뷰
def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request,'dojo/post_detail.html',{
        'post' : post,
    })


# CBV 샘플- STEP 2. 함수를 통해 뷰 생성
def generate_view_fn(model):
    def view_fn(request, id):
        instance = get_object_or_404(model,id=id)
        instance_name = model._meta.model_name
        template_name = '{}/{}_detail.html'.format(model._meta.app_label,instance_name)
        return render(request, template_name,{
            instance_name : instance,
        })

    return view_fn

post_detail = generate_view_fn(Post)


# CBV 샘플- STEP 3. CBV컨셉만 구현
class DetailView(object):
    # 이전 FBV를 CBV버전으로 컨셉만 간단히 구현. 같은 동작을 수행.
    def __init__(self, model):
        self.model = model

    def get_object(self, *args, **kwargs):
        return get_object_or_404(self.model, id=kwargs['id'])

    def get_template_name(self):
        return '{}/{}_detail.html'.format(self.model._meta.app_label,self.model._meta.model_name)

    def dispatch(self, request, *args, **kwargs):
        return render(request, self.get_template_name(), {
            self.model._meta.model_name: self.get_object(*args, **kwargs),
        })

    @classmethod
    def as_view(cls, model):
        def view(request, *args, **kwargs):
            self = cls(model)
            return self.dispatch(request, *args, **kwargs)
        return view

post_detail = DetailView.as_view(Post)


# CBV 샘플- STEP 4. CBV 구현
post_detail = DetailView.as_view(model=Post, pk_url_kwarg='id')
"""

# CBV 샘플- STEP 5. CBV를 좀 더 심플하게 구현 - urls.py 고침
post_detail = DetailView.as_view(model=Post)