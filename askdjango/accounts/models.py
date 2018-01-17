#accounts/models.py
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# 한 명의 유저에 대해 한 개의 프로필 = OneToOneField 설정
class Profile(models.Model):
    user = models.OneToOneField(User) #FIXME : BAD CASE!!!
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=50)