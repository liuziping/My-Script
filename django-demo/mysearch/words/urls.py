#coding:utf-8
from django.conf.urls import include, url
#from . import views                    # 1.7以下写法
from words import views as words_views  # 1.8以后推荐写法

urlpatterns = [
    # url(r'^index$', views.search),     # 老版写法
    url(r'^index$', words_views.search), # 推荐写法
]
