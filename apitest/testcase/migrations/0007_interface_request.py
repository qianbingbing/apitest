# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-06-16 07:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testcase', '0006_auto_20170616_1539'),
    ]

    operations = [
        migrations.AddField(
            model_name='interface',
            name='request',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
