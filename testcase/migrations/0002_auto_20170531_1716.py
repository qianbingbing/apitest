# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-05-31 09:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testcase', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testcase',
            name='params',
        ),
        migrations.AddField(
            model_name='testcase',
            name='params_key1',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='testcase',
            name='params_value1',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
