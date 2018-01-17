import re
from django.db import models
from django.forms import ValidationError


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
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=100, verbose_name='제목')
    content = models.TextField() #길이 제한 X
    tags = models.CharField(max_length=100, blank=False)
    lnglat = models.CharField(max_length=50, blank=True,
                              validators=[lnglat_validator],
                            help_text='위도, 경도 포맷으로 입력')
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True) #처음 저장될 때 저장
    updated_at = models.DateTimeField(auto_now=True) #갱신 될 때마다 저장

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.title