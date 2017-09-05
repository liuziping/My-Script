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
            name='Deploy',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=40, verbose_name='\u9879\u76ee\u540d\u79f0')),
                ('project_version', models.CharField(max_length=40, verbose_name='\u9879\u76ee\u7248\u672c')),
                ('version_desc', models.CharField(max_length=100, verbose_name='\u7248\u672c\u63cf\u8ff0')),
                ('applicant_id', models.IntegerField(default=1, verbose_name='\u7533\u8bf7\u4eba')),
                ('update_detail', models.TextField(verbose_name='\u66f4\u65b0\u8be6\u60c5')),
                ('is_version_back', models.BooleanField(default=False, verbose_name='\u662f\u5426\u4e3a\u56de\u9000\u7248\u672c')),
                ('status', models.IntegerField(default=0, verbose_name='\u4e0a\u7ebf\u72b6\u6001', choices=[(0, '\u7533\u8bf7'), (1, '\u7070\u5ea6'), (2, '\u4e0a\u7ebf'), (3, '\u53d6\u6d88\u4e0a\u7ebf')])),
                ('apply_time', models.DateTimeField(auto_now_add=True, verbose_name='\u7533\u8bf7\u65f6\u95f4')),
                ('deploy_time', models.DateTimeField(auto_now=True, verbose_name='\u4e0a\u7ebf\u5b8c\u6210\u65f6\u95f4')),
                ('assigned_to', models.ForeignKey(verbose_name='\u6307\u6d3e\u7ed9', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
