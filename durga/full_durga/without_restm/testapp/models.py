from django.db import models


class Employee(models.Model):
    eno = models.IntegerField()
    ename = models.CharField(max_length=69)
    esal = models.FloatField()
    eadd = models.CharField(max_length=96)
