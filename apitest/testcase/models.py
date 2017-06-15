from __future__ import unicode_literals
from django.db import models

# Create your models here.
#test case models
class Testcase(models.Model):
    case_id = models.IntegerField()
    title = models.CharField(max_length=20)
    desc = models.CharField(max_length=40)
    method = models.CharField(max_length=10)
    url = models.CharField(max_length=30)
    params = models.CharField(max_length=100,null=True)
    ex_result = models.CharField(max_length=100,null=True)

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
    developer = models.CharField(max_length=20)
    notes = models.CharField(max_length=100)


