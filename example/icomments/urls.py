# -*- coding:utf8 -*-
from django.conf.urls import url
from . import views

urlpatterns = [
    #url(r'^comment/$', views.comments, name='comment'),
    url(r'^comment_submit/$', views.comment_submit, name='comment_submit'),
    url(r'^comment_manage/(?P<type>[\w-]+)/$', views.comments_manage, name='comment_manage')
]
