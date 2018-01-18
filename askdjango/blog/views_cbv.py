import os
from django.views.generic import View, TemplateView, CreateView
from django.http import HttpResponse, JsonResponse
from .models import Post
from django import forms

#blog/forms.py


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

    def get_date(self):
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