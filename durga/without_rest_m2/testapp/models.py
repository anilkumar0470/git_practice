from django.db import models

# Create your models here.


class Student(models.Model):

    name = models.CharField(max_length=64)
    rollno = models.IntegerField()
    marks = models.IntegerField()
    girlfriend = models.CharField(max_length=64)
    boyfriend = models.CharField(max_length=64)

