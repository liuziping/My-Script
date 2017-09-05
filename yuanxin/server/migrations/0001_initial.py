# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Idc',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=10, verbose_name='IDC\u5b57\u6bcd\u7b80\u79f0')),
                ('idc_name', models.CharField(unique=True, max_length=100, verbose_name='IDC\u4e2d\u6587\u540d')),
                ('address', models.CharField(max_length=100, verbose_name='IDCd\u5730\u5740')),
                ('user', models.CharField(max_length=32, verbose_name='IDC\u8054\u7cfb\u4eba')),
                ('user_phone', models.CharField(max_length=20, verbose_name='\u8054\u7cfb\u4eba\u7535\u8bdd')),
                ('user_email', models.EmailField(max_length=32, verbose_name='\u8054\u7cfb\u4eba\u90ae\u4ef6')),
            ],
            options={
                'db_table': 'idc',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=32, verbose_name='\u4e1a\u52a1\u7ebf\u540d\u79f0')),
                ('pid', models.IntegerField(verbose_name='\u4e0a\u7ea7\u4e1a\u52a1\u7ebf', db_index=True)),
                ('module_letter', models.CharField(max_length=10, verbose_name='\u5b57\u6bcd\u7b80\u79f0')),
                ('op_interface', models.CharField(max_length=255, verbose_name='\u8fd0\u7ef4\u5bf9\u63a5\u4eba\uff1ausername1,username2')),
                ('dev_interface', models.CharField(max_length=255, verbose_name='\u4e1a\u52a1\u5bf9\u63a5\u4eba\uff1ausername1,username2')),
            ],
            options={
                'db_table': 'product',
            },
        ),
        migrations.CreateModel(
            name='Server',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('supplier', models.IntegerField(null=True)),
                ('manufacturers', models.CharField(max_length=50, null=True)),
                ('manufacture_date', models.DateField(null=True)),
                ('server_type', models.CharField(max_length=20, null=True)),
                ('sn', models.CharField(max_length=60, null=True, db_index=True)),
                ('os', models.CharField(max_length=50, null=True)),
                ('hostname', models.CharField(max_length=50, null=True, db_index=True)),
                ('inner_ip', models.CharField(max_length=32, unique=True, null=True)),
                ('mac_address', models.CharField(max_length=50, null=True)),
                ('ip_info', models.CharField(max_length=255, null=True)),
                ('server_cpu', models.CharField(max_length=250, null=True)),
                ('server_disk', models.CharField(max_length=100, null=True)),
                ('server_mem', models.CharField(max_length=100, null=True)),
                ('status', models.CharField(max_length=100, null=True, db_index=True)),
                ('remark', models.TextField(null=True)),
                ('service_id', models.IntegerField(null=True, db_index=True)),
                ('check_update_time', models.DateTimeField(null=True)),
                ('vm_status', models.IntegerField(null=True, db_index=True)),
                ('uuid', models.CharField(max_length=100, null=True, db_index=True)),
                ('idc', models.ForeignKey(to='server.Idc', null=True)),
                ('server_purpose', models.ForeignKey(to='server.Product', null=True)),
            ],
            options={
                'db_table': 'server',
            },
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=10, verbose_name='\u72b6\u6001\u540d')),
            ],
            options={
                'db_table': 'status',
            },
        ),
    ]
