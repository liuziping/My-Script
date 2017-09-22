#_*_ encoding:utf-8 _*_

from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

'''
class UserProfile(AbstractUser):
    name = models.CharField('中文名', max_length=30)
    phone = models.CharField('手机', max_length=11, null=True, blank=True)
    wechat = models.CharField('微信', max_length=20, null=True, blank=True)
    image = models.ImageField('头像', upload_to='image/%Y/%m', default='image/default.jpg')

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.username
'''

class EmailVerifyRecord(models.Model):
    SEND_TYPE = (
        ('register', '注册'),
        ('forget', '找回密码'),
        ('create', '创建账号'),
        ('order', '工单申请'),
    )
    code = models.CharField('验证码', max_length=20)
    email = models.EmailField('邮箱', max_length=50)
    send_type = models.CharField('发送类型', choices=SEND_TYPE, max_length=8)
    send_time = models.DateTimeField('发送时间', auto_now_add=True)

    class Meta:
        verbose_name = '邮箱验证码'
        verbose_name_plural = verbose_name

