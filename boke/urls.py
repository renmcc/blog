#!/usr/bin/env python
#coding:utf-8
#__time__: 2020/2/16 0:47
#__author__ = 'ren_mcc'

from django.conf.urls import url,include
from . import views


urlpatterns = [
    url(r'^', views.blog_title, name='blog_title'),
    url(r'(?P<article_id>\d)/$', views.blog_article,name="blog_detail"),
    url(r'hello/', views.hello,name="hello"),
]