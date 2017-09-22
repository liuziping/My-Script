#_*_ encoding:utf-8 _*_

from __future__ import unicode_literals

import xadmin
from xadmin import views

from .models import EmailVerifyRecord

class BaseSetting(object):
    # 主题修改
    enable_themes = True
    use_bootswatch = True

class GlobalSettings(object):
    site_title = '后台系统'                  #  后台标题
    site_footer = 'DevOps'                #  页脚
    menu_style = 'accordion'            # 菜单收起

class EmailVerifyRecordAdmin(object):
    list_display = ['code', 'email', 'send_type', 'send_time']
    search_fields = ['code', 'email', 'send_type']
    list_filter = ['code', 'email', 'send_type', 'send_time']

# 注册
xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)
