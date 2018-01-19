from django.db import models
from django import forms
from django.core.validators import MinLengthValidator
#dojo/models.py



#validator가 모델에 정의되면 admin에서도 validator동작하게 됨
def min_length_3_validator(value):
    if len(value) < 3:
        raise forms.ValidationError('3글자 이상 입력해주세요.') #예외만 발생하는 형태


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100, validators=[min_length_3_validator])
    content = models.TextField()
    user_agent = models.CharField(max_length=200)
    ip = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class GameUser(models.Model):
    server_name = models.CharField(max_length=10,
                                   choices = (
                                       ('A','A 서버'),
                                       ('B','B 서버'),
                                       ('C','C 서버'),
                                   ))
    user_name = models.CharField(max_length=20, validators=[MinLengthValidator(3)])

    class Meta:
        unique_together = [
            ('server_name','user_name'),
        ]