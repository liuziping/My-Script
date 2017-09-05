# _*_ coding: utf-8 _*_
import os
import json,logging

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect,JsonResponse,QueryDict,Http404
from django.core.urlresolvers import reverse
from django.views.generic.base import View
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.contrib.auth.models import Group
from django.core import serializers

# 自定义模块
from .forms import ApplyforReleaseForm, DeployForm
from dashboard.models import UserProfile
from .models import  Deploy
from utils.gitlab_utils import gl,get_user_projects
from utils.mixin_utils import LoginRequiredMixin 

logger = logging.getLogger("opsweb")
# Create your views here.


class ApplyForReleaseView(LoginRequiredMixin,View):
    '''
        申请发布
    '''
    def get(self, request):
        _, user_projects = get_user_projects(request)
        groups = Group.objects.filter(Q(name='test') | Q(name='sa'))
        assign_to_users = []
        for group in groups:
            assign_to_users.extend(group.user_set.all())
        return render(request, 'code/code-apply-for-release.html', {'user_projects': user_projects,
                                                                    'assign_to_users': assign_to_users})

    def post(self, request):
        _, user_projects = get_user_projects(request)
        groups = Group.objects.filter(Q(name='test') | Q(name='sa'))
        assign_to_users = []
        for group in groups:
            assign_to_users.extend(group.user_set.all())

        forms = ApplyforReleaseForm(request.POST)
        if forms.is_valid():
            name = request.POST.get('name', '')
            project_version = request.POST.get('project_version', '')
            version_desc = request.POST.get('version_desc', '')
            assigned_to = request.POST.get('assigned_to', '')
            update_detail = request.POST.get('update_detail', '')

            has_apply = Deploy.objects.filter(name=name.split('/')[1], status__lt=2)
            if has_apply:
                return render(request, 'code/code-apply-for-release.html',
                              {'errmsg': '该项目已经申请上线，但是上线还没有完成，上线完成后方可再次申请！'})
            try:
                apply_release = Deploy()
                apply_release.name = name.split('/')[1]
                apply_release.project_version = project_version
                apply_release.version_desc = version_desc
                apply_release.assigned_to_id = assigned_to
                apply_release.update_detail = update_detail
                apply_release.status = 0
                apply_release.applicant_id = request.user.id
                apply_release.save()
                return HttpResponseRedirect(reverse('apply_list'))
            except:
                logger.error("apply the release error: %s" % traceback.format_exc())
                return render(request, 'code/code-apply-for-release.html',{'errmsg':'申请失败，请查看日志'})
        else:
            return render(request, 'code/code-apply-for-release.html', {'forms': forms,
                                                                        'assign_to_users': assign_to_users,
                                                                        'user_projects': user_projects,
                                                                        'errmsg': '申请格式错误！'})



class ApplyListView(LoginRequiredMixin,View):
    '''
        申请发布列表
    '''
    def get(self, request):
        apply_list = Deploy.objects.filter(status__lt=2)
        search_keywords = request.GET.get('search_keywords', '')
        if search_keywords:
            apply_list = apply_list.filter(Q(name__icontains=search_keywords) |
                                           Q(update_detail__icontains=search_keywords) |
                                            Q(version_desc__icontains=search_keywords))
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(apply_list, 10, request=request)
        lists = p.page(page)
        return render(request, 'code/apply-list.html', {'page_obj': lists, 'p': p})

    def post(self, request):
        try:
            apply_id = request.POST.get('apply_id', '')
            Deploy.objects.filter(id=int(apply_id)).update(status=3)
            ret = {'code':0,'result':"取消上线成功！"}
        except:
            logger.error("Cancel the release error: %s" % traceback.format_exc())
            ret = {'code':1,'errmsg':"取消上线失败！"}
            
        return JsonResponse(ret ,safe=True)


class GetProjectVersionsView(LoginRequiredMixin,View):
    """
    获取指定项目的所有版本
    """
    def get(self, request):
        project_id = request.GET.get('project_id', '')
        tags = gl.project_tags.list(project_id=int(project_id.split('/')[0]))
        tags = [[tag.name,tag.message] for tag in tags]
        return  HttpResponse(json.dumps(tags), content_type='application/json')


class CodeReleaseStatus(LoginRequiredMixin,View):
    '''
        通过获取当前项目状态，执行代码发布功能
    '''

    def get(self, request):
        apply_id = request.GET.get('apply_id', 0)
        apply_release = Deploy.objects.get(id=apply_id)
        return render(request, 'code/code-release-status.html', {'apply_release': apply_release})

    def post(self, request):
        msg = '' 
        forms = DeployForm(request.POST)
        if forms.is_valid():
            apply_release = Deploy.objects.get(id=request.POST.get('id', 0))
            status = apply_release.status
            if apply_release:
                # 如果status为0,说明是申请状态，点击了仿真按钮，需要上线到仿真环境，并把status改为1
                if apply_release.status == 0:
                    #ret, msg = run_script_with_timeout("sh %s emulation %s %d %s" % (
                    #    os.path.join(SHELL_DIR, 'online.sh'), apply_release.name, 0, apply_release.project_version))
                    #if not ret:
                    #    return render(request, 'code/code-release-status.html', {'apply_release': apply_release,
                    apply_release.status = 1
                elif apply_release.status == 1:
                    #ret, msg = run_script_with_timeout("sh %s product %s %d" % (
                    #    os.path.join(SHELL_DIR, 'online.sh'), apply_release.name, 0))
                    #if not ret:
                    #    return render(request, 'code/code-release-status.html', {'apply_release': apply_release,
                    apply_release.status = 2
                else:
                    return HttpResponseRedirect(reverse('deploy_history'))

                apply_release.save()
                return render(request, 'code/code-release-status.html', {'apply_release': apply_release,
                                                                         'msg': msg})
        else:
            return HttpResponse(json.dumps({'errmsg': msg}))


class DeployHistoryView(LoginRequiredMixin,View):
    '''
        获取所有上线完成/失败的项目记录
    '''

    def get(self, request):
        deploy_histories = Deploy.objects.filter(status__gte=2).order_by('-deploy_time')
        search_keywords = request.GET.get('search_keywords', '')
        if search_keywords:
            deploy_histories = deploy_histories.filter(Q(name__icontains=search_keywords) |
                                                       Q(update_detail__icontains=search_keywords) |
                                                       Q(version_desc__icontains=search_keywords))
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(deploy_histories, 10, request=request)
        histories = p.page(page)
        return render(request, 'code/deploy-history.html', {'page_obj': histories, 'p': p})

