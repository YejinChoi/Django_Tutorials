import os
from django.views.generic import View, TemplateView, CreateView, ListView, DetailView, UpdateView, DeleteView
from django.http import HttpResponse, JsonResponse
from .models import Post
from django import forms
from django.core.urlresolvers import reverse_lazy

#blog/forms.py

# CBV : ListView 적용
#페이지 단위를 3개로 지정
post_list = ListView.as_view(model=Post, paginate_by=10)

# CBV : DetaillView 적용
post_detail = DetailView.as_view(model=Post)

# CBV : CreateView & UpdateView 적용
post_edit = UpdateView.as_view(model=Post, fields='__all__')
post_new = CreateView.as_view(model=Post)

# CBV : DeleteView 적용 + reverse_lazy 적용
# reverse_lazy : 모듈 import 시점에 url reverse가 필요할 때 사용
post_delete = DeleteView.as_view(model=Post, success_url=reverse_lazy('blog:post_list'))

"""
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'


class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    #success_url =

post_new = PostCreateView.as_view()

class PostListView1(View):
    def get(self,request):
        name = 'dd'
        html = self.get_template_string().format(name=name)
        return HttpResponse(html)

    def get_template_string(self):
        return '''
        <h1>AskDjango</h1>
        <p>{name}</p>
        '''

post_list1 = PostListView1.as_view()


class PostListView2(TemplateView):
    template_name = 'blog/post_list2.html'

    def get_context_data(self):
        #super() :
        context = super().get_context_data()
        context['name'] = 'yeah'
        return context


post_list2 = PostListView2.as_view()


class PostListView3(View):
    'CBV : JSON 형식 응답하기'
    def get(self,request):
        return JsonResponse(self.get_data(), json_dumps_params={'ensure_ascii' : False})

    def get_data(self):
        return{
            'message': 'Python',
            'items': ['dd', 'sdfsd', 'dsffwefwfsd'],
        }

post_list3 = PostListView3.as_view()

class ExcelDownloadView(View):
    'CBV : 엑셀 다운로드 응답하기'

    excel_path = '/other/path/excel.xls'

    def get(self,request):
        filename = os.path.basename(self.excel_path)
        with open(self.excel_path, 'rb') as f:
            response = HttpResponse(f, content_type='application/vnd.ms-excel')
            #필요한 응답헤더 세팅
            response['Content-Disposition'] = 'attachment;filename="{}"'.format(filename)
            return response

excel_download = ExcelDownloadView.as_view()
"""