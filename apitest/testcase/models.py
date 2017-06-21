from __future__ import unicode_literals
from django.db import models
from jsonfield import JSONField
import ast
# Create your models here.
#test case models
class Testcase(models.Model):
    interface_id = models.IntegerField(null = True)
    title = models.CharField(max_length=20)
    level = models.CharField(max_length=40,null=True)
    params = models.CharField(max_length=100,null=True)
    ex_result = models.CharField(max_length=100,null=True)
    tester = models.CharField(max_length=100,null = True)

#project models
class Project(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    desc = models.CharField(max_length=40)
    leader = models.CharField(max_length=10)
    remark = models.CharField(max_length=20)

#interface models
class Interface(models.Model):
    project_id = models.IntegerField()
    name = models.CharField(max_length=20)
    url = models.CharField(max_length=20)
    service_name = models.CharField(max_length=30)
    func = models.CharField(max_length=20)
    request = models.CharField(max_length=20,null=True)
    developer = models.CharField(max_length=20)
    notes = models.CharField(max_length=100)

class Report(models.Model):
    test_time = models.CharField(max_length=20)
    total_case = models.CharField(max_length=10)
    fail_case = models.CharField(max_length=10)
    success_case = models.CharField(max_length=10)
    test_result = models.CharField(max_length=10)
    rate = models.FloatField()
    detail_list = models.CharField(max_length=10000,null=True)
