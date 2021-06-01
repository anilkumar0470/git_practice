from django.db import models


class Employee(models.Model):
    name = models.CharField(max_length=30)
    emp_id = models.IntegerField()
    address = models.CharField(max_length=50)
    mobile_number = models.IntegerField()


