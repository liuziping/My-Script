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
from dashboard.models  import UserProfile
from django.conf import settings
from utils.mixin_utils import LoginRequiredMixin 
from utils.gitlab_utils import gl


logger = logging.getLogger("opsweb")

# 组列表
class GroupListView(LoginRequiredMixin,ListView):
    """
        查看组列表、添加组、删除组
    """
    @method_decorator(permission_required('dashboard',login_url='/'))
    def get(self, request):
        groups = Group.objects.all()
        keyword = request.GET.get('keyword', '')
        if keyword:
            groups = Group.objects.filter(name__icontains=keyword)

        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(groups, 10, request=request)
        groups = p.page(page)
        return render(request, 'user/group_list.html', {'page_obj': groups, 'p': p,'keyword':keyword})

    def post(self, request):
        ret = {'code' : 0}
        name = request.POST.get('name', None)
        if name:
            try:
                group = Group()
                group.name = name
                group.save()
                group = gl.groups.create({'name': name, 'path': name})
            except Exception as e:
                ret['code'] = 1                                                    
                ret['errmsg'] = e.args
                logger.debug("%s add group %s fail:%s" %(request.user,name,e.args))
        return JsonResponse(ret, safe=True)
    
    def delete(self,request):
        data = QueryDict(request.body)
        pid = data.get('id',None)
        res = Group.objects.filter(pk=pid).delete()
        if not res:
            ret = {'code': 0, 'result': '删除组成功'}
        else:
            ret = {'code': 1, 'errmsg': '删除组失败'}
        return JsonResponse(ret, safe=True)

class GroupUserView(LoginRequiredMixin,View):
    '''
        取出指定组下的所有用户信息
    '''
    @method_decorator(permission_required('dashboard',login_url='/'))
    def get(self, request):
        gid = request.GET.get('gid', None)
        try:
            group = Group.objects.get(pk=gid)
        except:
            return JsonResponse([], safe=False)

        users = group.user_set.all()
        user_list = [{'username':user.username, 'email':user.email,'id':user.id} for user in users]
        return JsonResponse(user_list, safe=False)
    '''
        将用户从用户组中删除
    '''
    def delete(self, request):
        ret = {'code': 0}
        data = QueryDict(request.body)
        uid = data.get('userid', None)
        gid = data.get('groupid', None)

        try:
            user = UserProfile.objects.get(pk=uid)
            group = Group.objects.get(pk=gid)
            group.user_set.remove(user)
        except UserProfile.DoesNotExist:
            ret['code'] = 1
            ret['errmsg'] = '用户不存在'
        except Group.DoesNotExist:
            ret['code'] = 2
            ret['errmsg'] = '用户组不存在'
        except Exception as e:
            ret['code'] = 3
            ret['errmsg'] =  e.args
        return JsonResponse(ret, safe=True)



class GroupPermView(LoginRequiredMixin,TemplateView):
    """
    编辑小组权限
    """
    template_name = 'user/group_perm.html'
    
    # 返回所有权限，并将当前组所拥有的权限选中
    def get_context_data(self, **kwargs):
        context = super(GroupPermView, self).get_context_data(**kwargs)
        context['gid'] = self.request.GET.get('id', None)
        context['group_has_permissions'] = self.get_group_permission()
        context['group_not_permissions'] = self.get_group_not_permission()
        return context
     
    # 获取当前用户所有权限，以列表形式返回
    def get_group_permission(self):
        gid = self.request.GET.get('id', None)
        try:
            group = Group.objects.get(pk=gid)
            return group.permissions.all() 
        except Group.DoesNotExist:
            raise Http404

    # 获取当前用户没有的权限，以列表形式返回
    def get_group_not_permission(self):
        gid = self.request.GET.get('id', None)
        try:
            group = Group.objects.get(pk=gid)
            all_perms = Permission.objects.all()
            perms = [perm for perm in all_perms if perm not in group.permissions.all()]
            return perms
        except:
            return JsonResponse([], safe=False)

    @method_decorator(permission_required('dashboard',login_url='/'))
    def post(self, request):
        ret = {'code' : 0, 'next_url':'/user/grouplist/'}
        permission_id_list = request.POST.getlist('perms_selected', [])
        gid = request.POST.get('gid', None)
        try:
            group = Group.objects.get(pk=gid)
            group.permissions = permission_id_list
        except Group.DoesNotExist:
            ret['code'] = 1 
            ret['errmsg'] = '组不存在'
        return render(request, settings.JUMP_PAGE, ret)  


