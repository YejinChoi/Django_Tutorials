from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.conf import settings
from . import views
from .forms import LoginForm

urlpatterns =[
    url(r'^signup/$',views.signup, name='signup'),
    url(r'^profile/$',views.profile, name='profile'),


    # 로그인/로그아웃 구현
    url(r'^login/$',auth_views.login, name='login',
        kwargs={
            'authentication_form' : LoginForm,
            'template_name': 'accounts/login_form.html'}),
    url(r'^logout/$',auth_views.logout, name='logout',
        kwargs={'next_page': settings.LOGIN_URL }),

]