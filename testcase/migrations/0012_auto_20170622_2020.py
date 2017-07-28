# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-06-22 12:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testcase', '0011_report_detail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='report',
            name='detail_list',
        ),
        migrations.RemoveField(
            model_name='report',
            name='test_result',
        ),
        migrations.AddField(
            model_name='report',
            name='report_id',
            field=models.CharField(max_length=40, null=True),
        ),
    ]