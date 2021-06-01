from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=30)
    rollno = models.IntegerField()
    marks = models.IntegerField()
    gf = models.CharField(max_length=30)
    bf = models.CharField(max_length=40)
