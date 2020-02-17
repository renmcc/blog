#!/usr/bin/env python
#coding:utf-8
#__time__: 2020/2/17 22:45
#__author__ = 'ren_mcc'
from django.conf.urls import url,include
from . import views
from django.conf import settings
from django.contrib.auth import views as auth_views


urlpatterns = [
    url(r'^login/$', auth_views.login, {"template_name": "account/login.html"},name='user_login'),
    url(r'^logout/$', auth_views.logout,{"template_name": "account/logout.html"}, name='user_logout'),
]