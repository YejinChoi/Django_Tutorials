#accounts/views.py
from django.conf import settings
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import SignupForm

# Create your views here.
# 회원가입 구현
def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect(settings.LOGIN_URL) # default : "/accounts/login/"
    else:
        form = SignupForm()

    return render(request, 'accounts/signup_form.html',{
        'form': form,
    })


# profile 함수가 호출될 때 login 되어있는 상황임을 보장
# 프로필 뷰에 login_required 장식자 추가
@login_required
def profile(request):
    return render(request,'accounts/profile.html')
