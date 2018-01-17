#accounts/models.py
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.
# 한 명의 유저에 대해 한 개의 프로필 = OneToOneField 설정
class Profile(models.Model):
    #user = models.OneToOneField(User) #FIXME : BAD CASE!!!
    #user = models.OneToOneField('auth.User') #FIXME : BAD CASE!!! - 프로젝트.모델명
    # 장고 사용자 인증에 사용되는 USER모델 변경을 지원하는게 settings.AUTH_USER_MODEL이므로 이거로 사용할 것!!
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=50)