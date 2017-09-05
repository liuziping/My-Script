# _*_ coding: utf-8 _*_
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser


class UserProfile(AbstractUser):
    name = models.CharField('中文名', max_length=30)
    phone = models.CharField('手机', max_length=11, null=True, blank=True)
    wechat = models.CharField('微信', max_length=20, null=True, blank=True)

    class Meta:
        verbose_name = 'userprofile'

    def __unicode__(self):
        return self.username

