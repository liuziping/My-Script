from django.conf.urls import include, url
from . import views
from dashboard import user,group,power

urlpatterns = [
    url(r'^login/', views.LoginView.as_view(), name='login'),
    url(r'^logout/', views.LogoutView.as_view(), name='logout'),
    url(r'^$', views.IndexView.as_view(),name="index"),

    url(r'user/',include([
        url(r'^userlist/$', user.UserListView.as_view(),name='user_list'),
        url(r'^userlistapi/$', user.UserListApiView.as_view(),name='user_list_api'),
        url(r'^useredit/$', user.UserEditView.as_view(),name='user_edit'),
        url(r'^usergroup/$', user.UserGroupView.as_view(),name='user_group'),
        url(r'^userperm/$', user.UserPermView.as_view(),name='user_perm'),
        url(r'^modifypasswd/$', user.ModifyPwdView.as_view(),name='modify_pwd'),
        url(r'^modifystatus/$', user.ModifyUserStatusView.as_view(),name='modify_status'),

        url('^user_messages/$', user.MyMessageView.as_view(), name='user_messages'),

        url(r'^grouplist/$', group.GroupListView.as_view(),name='group_list'),
        url(r'^groupuser/$', group.GroupUserView.as_view(),name='group_user'),
        url(r'^groupperm/$', group.GroupPermView.as_view(),name='group_perm'),

        url(r'^powerlist/$', power.PowerListView.as_view(),name='power_list'),
        url(r'^poweredit/$', power.PowerUpdateView.as_view(),name='power_edit'),
    ]))
]
