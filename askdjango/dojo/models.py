from django.db import models
from django import forms
#dojo/models.py


#validator가 모델에 정의되면 admin에서도 validator동작하게 됨
def min_length_3_validator(value):
    if len(value) < 3:
        raise forms.ValidationError('3글자 이상 입력해주세요.') #예외만 발생하는 형태

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100, validators=[min_length_3_validator])
    content = models.TextField()
    ip = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
