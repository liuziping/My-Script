# _*_ coding: utf-8 _*_

from django import forms
from django.contrib.auth.models import Group, Permission
from .models import UserProfile


class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=5,error_messages={'invalid': '用户名不能重复!'})

class UserProfileForm(forms.Form):
    username = forms.CharField(required=True, max_length=30)
    name = forms.CharField(required=True, max_length=30)
    phone = forms.CharField(required=True, max_length=11)
    email = forms.EmailField(required=True, max_length=20)

