# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-06-21 03:00
from __future__ import unicode_literals

from django.db import migrations, models
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('testcase', '0007_interface_request'),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_time', models.CharField(max_length=20)),
                ('total_case', models.CharField(max_length=10)),
                ('fail_case', models.CharField(max_length=10)),
                ('success_case', models.CharField(max_length=10)),
                ('test_result', models.CharField(max_length=10)),
                ('rate', models.FloatField()),
                ('details', jsonfield.fields.JSONField()),
            ],
        ),
    ]
