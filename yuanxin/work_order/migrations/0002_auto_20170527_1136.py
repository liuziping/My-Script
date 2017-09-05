# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work_order', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='workorder',
            options={'ordering': ['-complete_time'], 'verbose_name': 'work_order', 'verbose_name_plural': 'work_order'},
        ),
    ]
