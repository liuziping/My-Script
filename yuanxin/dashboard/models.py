# _*_ coding: utf-8 _*_
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser



class UserMessage(models.Model):
    user = models.IntegerField(default=0, verbose_name=u"接收用户")
    message = models.CharField(max_length=500, verbose_name=u"消息内容")
    has_read = models.BooleanField(default=False, verbose_name=u"是否已读")
    add_time = models.DateTimeField(auto_now_add=True, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"user_message"
        verbose_name_plural = verbose_name


class UserProfile(AbstractUser):
    name = models.CharField('中文名', max_length=30)
    phone = models.CharField('手机', max_length=11, null=True, blank=True)
    wechat = models.CharField('微信', max_length=20, null=True, blank=True)

    class Meta:
        verbose_name = 'userprofile'

    def __unicode__(self):
        return self.username

    def unread_messages(self):
        unread_messages = UserMessage.objects.filter(user=self.id, has_read=False)
        return unread_messages
