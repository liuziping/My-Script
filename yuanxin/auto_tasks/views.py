# encoding: utf-8
import json
import os,sys,logging,traceback
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponse,HttpResponseRedirect
from django.views.generic import View
from django.conf import settings
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from utils.mixin_utils import LoginRequiredMixin
from .models import AutoTasks, ExecResult
from .forms import TaskAddForm
from utils.ansible_api import AnsiblePlaybookAPI

# Create your views here.


logger = logging.getLogger("opsweb")

class TaskAddView(LoginRequiredMixin, View):
    def get(self, request):
         forms = TaskAddForm()
         return render(request, 'auto_tasks/task-add.html', {'forms': forms})

    def post(self, request):
        forms = TaskAddForm(request.POST, request.FILES)
        if forms.is_valid():
            name = forms.cleaned_data['name']
            playbook = forms.cleaned_data['playbook']

            auto_task = AutoTasks()
            auto_task.name = name
            auto_task.playbook = playbook
            auto_task.save()
            return HttpResponseRedirect(reverse('auto_tasks:list'))
        else:
            return render(request, 'auto_tasks/task-add.html', {'forms': forms,'errmsg': '必须填写处理结果！'})  



class TaskListView(View):
    def get(self, request):
        all_tasks = AutoTasks.objects.all()

        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(all_tasks, 10, request=request)
        tasks = p.page(page)
        return render(request, 'auto_tasks/task-list.html', {'page_obj': tasks, 'p': p})


class TaskExecuteView(View):
    """
    playbook执行
    """
    def post(self, request):
        task_id = request.POST.get('task_id', 0)
        task = AutoTasks.objects.get(id=int(task_id))
        print "path is %s " % task.playbook.path

        try:
                playbook = AnsiblePlaybookAPI(task.playbook.path)
                exec_result = playbook.run('/tmp/ansible.log', '/tmp/tmp_ansible.log')
                task.detail_result = exec_result['detail']
                task.status = 'Y'
                task.save()
        except:
                logger.error("insert AutoTasks  error: %s" % traceback.format_exc())
        
        simple = exec_result['simple']
        for record in simple:
            try:
                    task_result = ExecResult()
                    task_result.task = task
                    task_result.host = record
                    task_result.unreachable = simple[record]['unreachable']
                    task_result.skipped = simple[record]['skipped']
                    task_result.ok = simple[record]['ok']
                    task_result.changed = simple[record]['changed']
                    task_result.failures = simple[record]['failures']
                    task_result.save()
            except:
                logger.error("insert ExecResult  error: %s" % traceback.format_exc())
                

        return HttpResponse(json.dumps({'status': 0,
                                        'task_status': task.status,
                                        'task_exec_result': simple,
                                        'msg': '任务执行成功'}),
                            content_type="application/json")


class TaskExecDetailView(View):
    def get(self, request):
        task_id = request.GET.get('task_id', 0)
        print task_id
        task = ''
        try:
           task = AutoTasks.objects.get(id=int(task_id))
        except AutoTasks.DoesNotExist:
           pass
        return render(request, 'auto_tasks/task-exec-detail.html', {'task': task})

