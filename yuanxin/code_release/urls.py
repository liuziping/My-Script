# _*_ coding: utf-8 _*_
from django.conf.urls import url
from .views import *

urlpatterns = [
    url('^apply_for_release/$', ApplyForReleaseView.as_view(), name='apply_for_release'),
    url('^apply_list/$', ApplyListView.as_view(), name='apply_list'),
    url('^deploy_history/$', DeployHistoryView.as_view(), name='deploy_history'),
    url('^code_release_status/$', CodeReleaseStatus.as_view(), name='code_release_status'),
    # 获取某个项目的所有标签(版本)
    url('^get_project_versions/$', GetProjectVersionsView.as_view(), name='get_project_versions'),
]
