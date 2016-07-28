from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^index$', views.search),
 #   url(r'^$', views.search),
 #   url(r'^s/$', "words.views.search"),
]
