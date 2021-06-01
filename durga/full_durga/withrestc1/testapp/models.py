from django.db import models
# from django.core.exceptions import FieldDoesNotExist

class Employee(models.Model):
    eno = models.IntegerField()
    ename = models.CharField(max_length=30)
    esal = models.FloatField()
    eadd = models.CharField(max_length=50)


