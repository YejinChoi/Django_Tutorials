"""askdjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url , include
from django.contrib import admin
from django.conf import settings
from django.shortcuts import redirect
from django.views.generic import RedirectView
from django.conf.urls.static import static


#def root(request):
    #return redirect('blog:post_list')

urlpatterns = [
    #url(r'$',root, name='root'),
    url(r'^$', lambda r:redirect('blog:post_list'), name='root'), #url(r'$',root, name='root')와 동일
    #url(r'^$',RedirectView.as_view(pattern_name='blog:post_list')),

    url(r'^admin/', admin.site.urls),
    url(r'^blog/', include('blog.urls', namespace='blog')),
    url(r'^dojo/', include('dojo.urls', namespace='dojo')),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^shop/', include('shop.urls',namespace='shop')),
]

#settings.DEBUG=False 에서는 static 함수에서 빈 리스트를 리턴
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# 해당 페이지의 템플릿에 body가 있어야 debug_toolbar가 주입됨
if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]