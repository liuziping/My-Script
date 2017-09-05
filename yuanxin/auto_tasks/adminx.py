# encoding: utf-8
import xadmin

from .models import AutoTasks, ExecResult


class AutoTasksAdmin(object):
    list_display = ['name', 'playbook', 'detail_result', 'add_time', 'exec_time']
    search_fields = ['name', 'playbook', 'detail_result']
    list_filter = ['name', 'playbook', 'detail_result', 'add_time', 'exec_time']


class ExecResultAdmin(object):
    list_display = ['task', 'host', 'unreachable', 'skipped', 'ok', 'changed', 'failures']
    search_fields = ['task', 'host', 'unreachable', 'skipped', 'ok', 'changed', 'failures']
    list_filter = ['task', 'host', 'unreachable', 'skipped', 'ok', 'changed', 'failures']


xadmin.site.register(AutoTasks, AutoTasksAdmin)
xadmin.site.register(ExecResult, ExecResultAdmin)
