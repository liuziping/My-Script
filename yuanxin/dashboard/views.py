#coding:utf-8

# 系统自带模块导入
from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect,JsonResponse,QueryDict,Http404
from django.core.urlresolvers import reverse
from django.views.generic import View,TemplateView, ListView, RedirectView, FormView
from django.db.models import Q
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import Group, Permission
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required, permission_required

from django.core import serializers
import traceback,json,logging

# 自定义模块导入
from .models import UserProfile
from .forms import LoginForm


logger = logging.getLogger("opsweb")


class LoginView(View):
    '''
        登录模块
    '''

    def get(self, request):
        return render(request, "public/login.html")

    def post(self, request):
        ret = {"code": 0}
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = request.POST.get("username", None)
            password = request.POST.get("password", None)
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    ret['next_url'] = '/'
                else:
                    ret['code'] = 1
                    ret['errmsg'] = '用户被禁用'
            else:
                ret['code'] = 1
                ret['errmsg'] = '用户名或密码错误'
        else:
                ret['code'] = 1
                ret['errmsg'] = '用户名或密码格式不符合要求'
            
        return JsonResponse(ret, safe=True)

class LogoutView(View):
    '''
        登出
    '''
    @method_decorator(login_required)
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse("login"))


class IndexView(View):
    @method_decorator(login_required)
    def get(self, request):
        return render(request,'public/index.html')
