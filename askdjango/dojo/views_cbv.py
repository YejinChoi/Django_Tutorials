from django.http import HttpResponse
from django.views.generic import View, TemplateView

# HttpResponse로 응답
class PostListView1(View):
    def get(self, request):
        name = '공유'
        html = self.get_template_string().format(name=name)
        return HttpResponse(html)

    def get_template_string(self):
        return '''
            <h1>AskDjango</h1>
            <p>{name}</p>
            <p>여러분의 파이썬&장고 페이스메이커가 되어드리겠습니다.</p>
        '''


post_list1 = PostListView1.as_view()

# 템플릿으로 응답
class PostListView2(TemplateView):
    template_name = 'dojo/post_list.html'

    def get_context_data(self):
        context = super().get_context_data()
        context['name'] = '공유'
        return context


post_list2 = PostListView2.as_view()

# Json통한 응답
class PostListView3(View):
    'CBV : JSON 형식 응답하기'
    def get(self,request):
        return JsonResponse(self.get_data(),json_dumps_params={'ensure_ascii' : False})

    def get_data(self):
        return {
            'messages': 'Python3-Django-Tutorial',
            'items': ['Python3.6.3', 'pycharm', 'community']
        }
post_list3 = PostListView3.as_view()

class ExcelDownloadView(View):
    'CBV : 엑셀 다운로드 응답하기'

    excel_path = '/other/path/excel.xls'

    def get(self, request):
        filename = os.path.basename(self.excel_path)
        with open(self.excel_path, 'rb') as f:
            response = HttpResponse(f, content_type='application/vnd.ms-excel')
            # 필요한 응답헤더 세팅
            response['Content-Disposition'] = 'attachment;filename="{}"'.format(filename)
            return response


excel_download = ExcelDownloadView.as_view()