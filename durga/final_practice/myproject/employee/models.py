from django.db import models


class EmployeeDetails(models.Model):
    ename = models.CharField(max_length=30)
    eid = models.IntegerField()
    esal = models.FloatField()
    eadd = models.TextField()
