import re
from django.db import models
from django.forms import ValidationError
from django.conf import settings
from django.core.urlresolvers import reverse


def lnglat_validator(value):
    if not re.match(r'^([+-]?\d+\.?\d*),([+-]?\d+\.?\d*)$',value):
        raise ValidationError('Invalid LngLat Type')


# Create your models here.
# 필수 필드 - blank=False 나 null=False
class Post(models.Model):
    STATUS_CHOICES = (
        ('d','Draft'),
        ('p','Published'),
        ('w','Withdrawn'),
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='blog_post_set')
    # related_name='+' 로 주는 경우, related_name을 포기하겠다는 말 == user.post_set.all() 못씀
    # 대신 shop.models.Post.objects.filter(user=user)는 사용 가능

   #author = models.CharField(max_length=100)
    title = models.CharField(max_length=100, verbose_name='제목')
    content = models.TextField() #길이 제한 X
    tags = models.CharField(max_length=100, blank=True)
    lnglat = models.CharField(max_length=50, blank=True,
                              validators=[lnglat_validator],
                            help_text='위도, 경도 포맷으로 입력')
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    tag_set = models.ManyToManyField('Tag',blank=True) #관련 모델 클래스로 many to many 지정 - 모델 필드 문자열로 지정 가능하므로 이거로 릴레이션 지정할 것
    created_at = models.DateTimeField(auto_now_add=True) #처음 저장될 때 저장
    updated_at = models.DateTimeField(auto_now=True) #갱신 될 때마다 저장
    photo = models.ImageField(blank=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.title

    # 특정 모델 레코드에 대한 url을 얻는 함수 - 꼭 구현할 것
    def get_absolute_url(self):
        return reverse('blog:post_detail',args=[self.id])


class Comment(models.Model):
    post = models.ForeignKey(Post)
    author = models.CharField(max_length=20)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Tag(models.Model):
    name = models.CharField(max_length=50,unique=True)

    def __str__(self): # 해당 태그명이 보여지게 하도록
        return self.name

