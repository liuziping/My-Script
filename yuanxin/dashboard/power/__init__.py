#coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect,JsonResponse,QueryDict,Http404
from django.core.urlresolvers import reverse
from django.views.generic import View,TemplateView, ListView, RedirectView, FormView
from django.db.models import Q
from django.contrib.auth.models import Permission,Group
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from pure_pagination.mixins import PaginationMixin
from django.core import serializers
import traceback,json,logging
from django.utils.decorators import method_decorator
from  django.contrib.auth.decorators import  permission_required

# 自定义模块导入
from  dashboard.models  import UserProfile
from django.conf import settings
from utils.mixin_utils import LoginRequiredMixin 

# 权限列表
class PowerListView(LoginRequiredMixin,ListView):
    
    """
        权限列表
    """
    @method_decorator(permission_required('dashboard',login_url='/'))
    def get(self, request):
        perms = Permission.objects.all()
        keyword = request.GET.get('keyword', '')
        if keyword:
            perms = Permission.objects.filter(Q(name__icontains=keyword)|
                                        Q(codename__icontains=keyword))

        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(perms, 10, request=request)
        perms = p.page(page)
        return render(request, 'user/power_list.html', {'page_obj': perms, 'p': p,'keyword':keyword})

    """
    权限添加
    获取参数及传入代码有待优化
    """
    def post(self, request):
        name  = request.POST.get('name', '')
        codename  = request.POST.get('codename', '')
        content_type  = request.POST.get('content_type', '')
        res = Permission.objects.create(name=name,codename=codename,content_type_id=content_type)
        if res:
            ret = {'code':0,'result':'添加权限成功'}
        else:
            ret = {'code': 1, 'errmsg':'添加权限失败'}
        return  JsonResponse(ret, safe=True)

    """
       删除权限
    """
    def delete(self,request):
        data = QueryDict(request.body)
        pid = data.get('id',None)
        res = Permission.objects.filter(pk=pid).delete()
        if res:
            ret = {'code': 1, 'errmsg': '删除权限失败'}
        else:
            ret = {'code': 0, 'result': '删除权限成功'}

        return JsonResponse(ret, safe=True)
   


class PowerUpdateView(LoginRequiredMixin,TemplateView):
    """
        更新权限
    """
    template_name = "user/power_edit.html"
    
    def get_context_data(self,**kwargs):
        context = super(PowerUpdateView,self).get_context_data(**kwargs)
        pid = self.request.GET.get('id',None)
        context['perm_obj'] =  self.get_perm_obj(pid)
        return context

    @method_decorator(permission_required('dashboard',login_url='/'))
    def post(self,request):
        # 此处因为只更新两个字段，暂时采用比较原始的写法，后期优化
        pid = request.POST.get('id',None)
        # 采用先取出数据，然后在对具体的列修改
        perm_obj = self.get_perm_obj(pid)
        perm_obj.name = request.POST.get('name',None)
        perm_obj.codename = request.POST.get('codename',None)
        res = perm_obj.save()
        if not res:
            ret = {'code':0,"next_url":"/user/powerlist/",'result':'更新权限成功'}
        else:
            ret = {'code':1,"next_url":"/user/powerlist/",'errmsg':'更新权限失败'}
        return  render(request,settings.JUMP_PAGE,ret)
    

    def get_perm_obj(self,pid):
        try:
            return Permission.objects.get(pk=pid)
        except Permission.DoesNotExist:
            raise Http404

    



   
