from django.contrib.auth.forms import UserCreationForm

# 회원가입시에 이메일 추가 입력
class SignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('email',)