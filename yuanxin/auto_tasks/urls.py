# encoding: utf-8

# _*_ coding: utf-8 _*_
from django.conf.urls import url
from .views import *

urlpatterns = [
    url('^add/$', TaskAddView.as_view(), name='add'),
    url('^list/$', TaskListView.as_view(), name='list'),
    url('^exec_detail/$', TaskExecDetailView.as_view(), name='exec_detail'),

    # 任务执行的url
    url('^task_execute/$', TaskExecuteView.as_view(), name='task_execute'),
]
