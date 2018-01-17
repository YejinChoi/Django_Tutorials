from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Post


# Register your models here.
@admin.register(Post)
#  #admin.site.register(Post)와 같은 표현
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'content_size','status','created_at', 'updated_at']

    actions=['make_published'] #action을 수행하기 위함

    def content_size(self,post):
        return mark_safe('<strong>{}</strong>글자'.format(len(post.title)))
    content_size.short_description = '글자수'

    def make_published(self, request, queryset):
        updated_count = queryset.update(status='p') #QuerySet.update
        self.message_user(request,'{}건의 포스팅을 Published로 변경'.format(updated_count)) #django message framework 활용
    make_published.short_description = '선택한 포스팅을 Published로 변경하는 작업입니다.'


#admin.site.register(Post)