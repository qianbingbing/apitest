from __future__ import unicode_literals
from django.db import models
from jsonfield import JSONField
import ast
# Create your models here.
#test case models
class Testcase(models.Model):
    interface_id = models.IntegerField(null = True)
    title = models.CharField(max_length=20)
    precondition = models.CharField(max_length=1000,null=True)
    level = models.CharField(max_length=40,null=True)
    params = models.CharField(max_length=1000,null=True)
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
    report_id = models.CharField(max_length=40,null=True)
    test_time = models.CharField(max_length=20)
    interface_number = models.CharField(max_length=10,null=True)
    total_case = models.CharField(max_length=10)
    fail_case = models.CharField(max_length=10)
    success_case = models.CharField(max_length=10)
    rate = models.CharField(max_length=10)

class Report_detail(models.Model):
    report_id =models.CharField(max_length=40)
    interface_id = models.CharField(max_length=20,null=True)
    interface_name = models.CharField(max_length=40,null=True)
    func_name = models.CharField(max_length=20)
    interface_result = models.CharField(max_length=10)
    case_detail = models.CharField(max_length=10000)
