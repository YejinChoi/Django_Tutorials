from django.conf.urls import url
from . import views
from . import views_cbv
#blog/urls.py

urlpatterns = [
    #url(r'^$',views.post_list, name='post_list'),

    url(r'^$', views_cbv.post_list, name='post_list'),

    url(r'^sum/(?P<x>\d+)/$', views.mysum),
    url(r'^sum/(?P<x>\d+)/(?P<y>\d+)/$',views.mysum),
    url(r'^sum/(?P<numbers>[\d/]+)/$', views.mysum),
    url(r'^hello/(?P<name>[ㄱ-힣]+)/(?P<age>\d+)/$',views.hello),
    url(r'^new/$', views.post_new, name='post_new'),
    url(r'^(?P<id>\d+)/edit/$', views.post_edit, name='post_edit'),

    url(r'^list/$', views.post_list,name='post_list'),
    url(r'^list1/$', views.post_list1),
    url(r'^list2/$', views.post_list2),
    url(r'^list3/$', views.post_list3),
    url(r'^excel/$', views.excel_download),

    url(r'^cbv/list1/$', views_cbv.post_list1),
    url(r'^cbv/list2/$', views_cbv.post_list2),
    url(r'^cbv/list3/$', views_cbv.post_list3),
    url(r'^cbv/excel/$', views_cbv.excel_download),
    url(r'^cbv/new/$',views_cbv.post_new),

    #url(r'^(?P<id>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^(?P<pk>\d+)/$', views_cbv.post_detail, name='post_detail'),
]