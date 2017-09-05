# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkOrder',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100, verbose_name='\u5de5\u5355\u6807\u9898')),
                ('type', models.IntegerField(default=0, verbose_name='\u5de5\u5355\u7c7b\u578b', choices=[(0, '\u6570\u636e\u5e93'), (1, 'WEB\u670d\u52a1'), (2, '\u8ba1\u5212\u4efb\u52a1'), (3, '\u914d\u7f6e\u6587\u4ef6'), (4, '\u5176\u5b83')])),
                ('order_contents', models.TextField(verbose_name='\u5de5\u5355\u5185\u5bb9')),
                ('status', models.IntegerField(default=0, verbose_name='\u5de5\u5355\u72b6\u6001', choices=[(0, '\u7533\u8bf7'), (1, '\u5904\u7406\u4e2d'), (2, '\u5b8c\u6210'), (3, '\u5931\u8d25')])),
                ('result_desc', models.TextField(null=True, verbose_name='\u5904\u7406\u7ed3\u679c', blank=True)),
                ('apply_time', models.DateTimeField(auto_now_add=True, verbose_name='\u7533\u8bf7\u65f6\u95f4')),
                ('complete_time', models.DateTimeField(auto_now=True, verbose_name='\u5904\u7406\u5b8c\u6210\u65f6\u95f4')),
                ('applicant', models.ForeignKey(related_name='work_order_applicant', verbose_name='\u7533\u8bf7\u4eba', to=settings.AUTH_USER_MODEL)),
                ('assign_to', models.ForeignKey(verbose_name='\u6307\u6d3e\u7ed9', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-complete_time'],
                'verbose_name': '\u5de5\u5355',
                'verbose_name_plural': '\u5de5\u5355',
            },
        ),
    ]
