#!/usr/bin/env python
#coding:utf-8
#__time__: 2020/2/22 13:07
#__author__ = 'ren_mcc'

from django import forms
from .models import ArticleColumn

class ArticleColumnForm(forms.ModelForm):
    class Meta:
        model = ArticleColumn
        fields = ('column',)