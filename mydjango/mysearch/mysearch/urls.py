from django.conf.urls import include, url
from django.contrib import admin
from blog import views as blog_view

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^search/', include('words.urls')),
    url(r'^$', "blog.views.index",name='index'),
    url(r'^add/$', blog_view.add, name='add'),
    url(r'^sum/(\d+)/(\d+)/$', blog_view.sum, name='sum')
]
