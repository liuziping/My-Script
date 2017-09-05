#coding:utf-8
from django.views.generic import TemplateView, View, ListView
from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse, Http404
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render
from django.core.urlresolvers import reverse
import json,logging

# 自定义模块
from server.models import Idc
from server.forms import IdcForm
from django.conf import settings
from utils.mixin_utils import LoginRequiredMixin


logger = logging.getLogger('opsweb')

class AddIdcView(LoginRequiredMixin,TemplateView):
    '''
        添加IDC
    '''
    template_name = "server/add_idc.html"

    def get(self,request,*args, **kwargs):
        return super(AddIdcView, self).get(request,*args,**kwargs)

    def post(self,request):
        ret = {"code":0,"next_url":reverse("idc_list")}
        form = IdcForm(request.POST)
        if form.is_valid():
            try:
                idc = Idc(**form.cleaned_data)
                idc.save() 
            except Exception as e:
                msg = "user {} add IDC error:{}".format(request.user.username,e.args)
                logger.error(msg)
                ret['code'] = 1
                ret['errmsg']  = msg

        else:
            msg = "user {} add checked failed:{}".format(request.user.username,form.errors.as_json())
            logger.error(msg)
            ret['code'] = 1
            ret['errmsg'] = msg
            
        return render(request, settings.JUMP_PAGE, ret)  

            
class IdcListView(LoginRequiredMixin,ListView):
    model = Idc
    template_name = "server/idc_list.html"
   
    def get(self,request,*args, **kwargs):
        return super(IdcListView, self).get(request,*args,**kwargs)

