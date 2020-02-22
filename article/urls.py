#!/usr/bin/env python
#coding:utf-8
#__time__: 2020/2/22 13:13
#__author__ = 'ren_mcc'

from django.conf.urls import url,include
from . import views


urlpatterns = [
    url(r'article-column/$', views.article_column, name='article_column'),
    url(r'rename-column/$', views.rename_article_column, name='rename_article_column'),
    url(r'del-column/$', views.del_article_column, name='del_article_column'),
]