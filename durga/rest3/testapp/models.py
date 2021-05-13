from django.db import models

# Create your models here.


# class TestEmployee(models.Model):
#     ename = models.CharField(max_length=64)
#     eno = models.IntegerField()
#     esal = models.FloatField()
#     eadd = models.CharField(max_length=64)

class Employee(models.Model):
    username = models.CharField(max_length=64)
    fname = models.CharField(max_length=64)
    lname = models.CharField(max_length=64)
    salary = models.FloatField()
    emp_id = models.IntegerField()
    email = models.EmailField()

