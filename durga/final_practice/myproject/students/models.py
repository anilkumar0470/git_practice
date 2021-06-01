from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=30)
    phone =models.IntegerField()
    standard = models.IntegerField()
    address = models.CharField(max_length=60)
