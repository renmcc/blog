#!/usr/bin/env python
#coding:utf-8
#__time__: 2020/2/17 22:47
#__author__ = 'ren_mcc'
from django import forms

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)