#coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect,JsonResponse,QueryDict,Http404
from django.core.urlresolvers import reverse
from django.views.generic import View,TemplateView, ListView, RedirectView, FormView
from django.db.models import Q
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import Permission,Group
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from pure_pagination.mixins import PaginationMixin
from django.core import serializers
import traceback,json,logging

from django.utils.decorators import method_decorator
from  django.contrib.auth.decorators import  permission_required


# 自定义模块导入
from dashboard.models  import UserProfile,UserMessage  
from dashboard.forms import UserProfileForm
from django.conf import settings
from utils.mixin_utils import LoginRequiredMixin  
from utils.gitlab_utils import gl

logger = logging.getLogger("opsweb")

# 通过ListView继承并简化TemplateView的操作
class UserListView(LoginRequiredMixin,ListView):
    """ 
        查看所有用户
    """
    @method_decorator(permission_required('dashboard',login_url='/'))
    def get(self, request):
        users = UserProfile.objects.all()
        keyword = request.GET.get('keyword', '') 
        if keyword:
            users = UserProfile.objects.filter(Q(name__icontains=keyword)|
                                        Q(username__icontains=keyword))

        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1 

        p = Paginator(users, 10, request=request)
        users = p.page(page)
        return  render(request, 'user/user_list.html', {'page_obj': users, 'p': p,'keyword':keyword})
   
    """ 
        添加用户
    """
    @method_decorator(permission_required('dashboard',login_url='/'))
    def post(self,request):
            username = request.POST.get('username', '') 
            name = request.POST.get('name', '') 
            phone = request.POST.get('phone', '') 
            email = request.POST.get('email', '') 
           
            try:
                user = UserProfile()
                user.username = username
                user.name = name
                user.email = email
                user.phone = phone
                user.password = make_password("12345678")
                user.is_active = True
                user.save()

                # 创建gitlab账户
                user = gl.users.create({'username': username,
                                    'password': "12345678",
                                    'email': email,
                                    'name': name})

                ret =   {'code':0,'result': '添加用户 {0} 成功，用户名密码已经发送到 {1} 邮箱!'.format(name, email)}

            except:
                logger.error("create user  error: %s" % traceback.format_exc())
                ret =  {'code': 1, 'errmsg': '添加用户失败'}
            return JsonResponse(ret,safe=True)    
    
    """ 
       删除用户
    """
    def delete(self,request):
        data = QueryDict(request.body)
        uid = data.get('id',None)
        try:
            res = UserProfile.objects.filter(pk=uid).delete()
            ret = {'code': 0, 'result': '删除用户成功'}
        except:
            logger_debug.error("delete user  error: %s" % traceback.format_exc())
            ret = {'code': 1, 'errmsg': '删除用户失败'}

        return JsonResponse(ret, safe=True)

# 获取所有与用户信息，以json的方式返回
class UserListApiView(View):
    def get(self, request):
        users = UserProfile.objects.all()
        return HttpResponse(serializers.serialize('json', users), content_type='application/json')

class UserEditView(LoginRequiredMixin,TemplateView):
    """
        更新用户基本信息
    """
        
    template_name = "user/user_edit.html"
    
    def get_context_data(self,**kwargs):
        context = super(UserEditView,self).get_context_data(**kwargs)
        uid = self.request.GET.get('uid',None)
        context['user_obj'] =  self.get_user_obj(uid)
        return context

    @method_decorator(permission_required('dashboard',login_url='/'))
    def post(self,request):
        data =  request.POST.dict()
        uid = data['id']
        print data
        try:
            UserProfile.objects.filter(pk=uid).update(**data) 
            ret = {'code':0,"next_url":"/user/userlist/",'result':'更新用户成功'}
        except:
            ret = {'code':1,"next_url":"/user/userlist/",'errmsg':'更新用户失败'}
            logger.error("update user  error: %s" % traceback.format_exc())
        return  render(request,settings.JUMP_PAGE,ret)
    

    def get_user_obj(self,uid):
        try:
            return UserProfile.objects.get(pk=uid)
        except UserProfile.DoesNotExist:
            raise Http404

# 用户的组管理
class UserGroupView(LoginRequiredMixin,TemplateView):
    template_name = 'user/user_group.html'

    # 返回所有组，并将当前用户所拥有的组显示
    def get_context_data(self, **kwargs):
        context = super(UserGroupView, self).get_context_data(**kwargs)
        context['uid'] = self.request.GET.get('uid', None)
        context['user_has_groups'] = self.get_user_group()
        context['user_not_groups'] = self.get_user_not_group()
        return context 

    # 获取当前用户所有组，以列表形式返回
    def get_user_group(self):
        uid = self.request.GET.get('uid', None)
        try:
            user = UserProfile.objects.get(pk=uid)
            return user.groups.all()
        except UserProfile.DoesNotExist:
            raise Http404
    
    # 获取当前用户没有的组，以列表形式返回
    def get_user_not_group(self):
        uid = self.request.GET.get('uid', None)
        try:
            user = UserProfile.objects.get(pk=uid)
            all_group = Group.objects.all()
            groups = [group for group in all_group if group not in user.groups.all()]
            return groups
        except:
            return JsonResponse([], safe=False)

    @method_decorator(permission_required('dashboard',login_url='/'))
    def post(self, request):
        ret = {'code' : 0, 'next_url':'/user/userlist/'}
        group_id_list = request.POST.getlist('groups_selected', [])
        uid = request.POST.get('uid', None)
        try:
            user = UserProfile.objects.get(pk=uid)
            user.groups = group_id_list
        except:
            ret['code'] = 1
            ret['errmsg'] = '组更新失败'
            logger.error("edit  user group error: %s" % traceback.format_exc())
        return render(request, settings.JUMP_PAGE, ret)


# 用户的权限管理
class UserPermView(LoginRequiredMixin,TemplateView):
    template_name = 'user/user_perm.html'

    # 返回所有权限，并将当前用户所拥有的权限
    def get_context_data(self, **kwargs):
        context = super(UserPermView, self).get_context_data(**kwargs)
        context['uid'] = self.request.GET.get('uid', None)
        context['user_has_permissions'] = self.get_user_permission()
        context['user_not_permissions'] = self.get_user_not_permission()
        return context

    # 获取当前用户所有权限，以列表形式返回
    def get_user_permission(self):
        uid = self.request.GET.get('uid', None)
        try:
            user = UserProfile.objects.get(pk=uid)
            return user.user_permissions.all()
        except UserProfile.DoesNotExist:
            raise Http404
    
    # 获取当前用户没有的权限，以列表形式返回
    def get_user_not_permission(self):
        uid = self.request.GET.get('uid', None)
        try:
            user = UserProfile.objects.get(pk=uid)
            all_perms = Permission.objects.all()
            perms = [perm for perm in all_perms if perm not in user.user_permissions.all()]
            return perms
        except:
            return JsonResponse([], safe=False)

    @method_decorator(permission_required('dashboard',login_url='/'))
    def post(self, request):
        ret = {'code' : 0, 'next_url':'/user/userlist/'}
        permission_id_list = request.POST.getlist('perms_selected', [])
        uid = request.POST.get('uid', None)
        try:
            user = UserProfile.objects.get(pk=uid)
            user.user_permissions = permission_id_list
        except:
            ret['code'] = 1
            ret['errmsg'] = '权限更新失败'
            logger.error("create user  error: %s" % traceback.format_exc())
        return render(request, settings.JUMP_PAGE, ret)



class ModifyPwdView(LoginRequiredMixin,View):
    """
        重置密码
    """

    @method_decorator(permission_required('dashboard',login_url='/'))
    def get(self,request):
        uid = request.GET.get('uid',None)
        return render(request,'user/change_passwd.html',{'uid':uid})
        

    def post(self, request):
        uid = request.POST.get('uid',None)
        pwd1 = request.POST.get("password1", "")
        pwd2 = request.POST.get("password2", "")
        if pwd1 != pwd2:
              return render(request, "user/change_passwd.html", {"msg": "两次密码不一致，你可长点儿心吧！"})
            
        try:
            user = UserProfile.objects.get(pk=uid)
            user.password = make_password(pwd1)
            user.save()
             
            # 修改用户的gitlab密码
            gitlab_user = gl.users.list(username=user.username)[0]
            gitlab_user.password = pwd2
            gitlab_user.save()
            return  HttpResponseRedirect(reverse('index'))
        except:
            logger.error("change_passwd error: %s" % traceback.format_exc())
            return render(request, "user/change_passwd.html", {"msg": "密码修改失败"})
            



class ModifyUserStatusView(LoginRequiredMixin,View):
    """
        修改状态
    """
    def post(self, request):
        ret = {"status":0}
        user_id = request.POST.get('user_id', None)
        try:
            user = User.objects.get(pk=user_id)
            if user.is_active:
                user.is_active = False
            else:
                user.is_active = True
            user.save()
        except User.DoesNotExist:
            res['status'] = 1
            res['errmsg'] = "USER IS NOT EXIST"
        return JsonResponse(ret,safe=True)


class MyMessageView(LoginRequiredMixin, View):
    """
    我的消息
    """
    def get(self, request):
        all_messages = UserMessage.objects.filter(user=request.user.id)

        # 用户进入个人消息后清空未读消息的记录
        all_unread_messages = UserMessage.objects.filter(user=request.user.id, has_read=False)
        for unread_message in all_unread_messages:
            unread_message.has_read = True
            unread_message.save()

        # 对个人消息进行分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(all_messages, 5, request=request)

        messages = p.page(page)
        return render(request, 'user/user_message.html', {
            "page_obj": messages
        })
