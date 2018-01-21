from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Profile

# 회원가입시에 이메일 추가 입력
class SignupForm(UserCreationForm):
    phone_number = forms.CharField()
    address = forms.CharField()

    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('email',)

    # 회원가입 시에 전화번호와 주소 입력 추가 구현
    def save(self):
        user = super().save()
        profile = Profile.objects.create(
            user = user,
            phone_number = self.cleaned_data['phone_number'],
            address = self.cleaned_data['address'])
        return user