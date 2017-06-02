from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Testcase(models.Model):
    case_id = models.IntegerField()
    title = models.CharField(max_length=20)
    desc = models.CharField(max_length=40)
    method = models.CharField(max_length=10)
    url = models.CharField(max_length=30)
    params = models.CharField(max_length=100,null=True)
    ex_result = models.CharField(max_length=100,)