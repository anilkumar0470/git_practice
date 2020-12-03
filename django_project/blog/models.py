from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth.models import User
from django.contrib.auth.models import User

# Create your models here.
#  ORM - object relation model.


# class Post(models.Model):
#     title = models.CharField(max_length=100)
#     content = models.TextField()
#     date_posted = models.DateTimeField(default=timezone.now)
#     author = models.ForeignKey(User, on_delete=models.CASCADE)

# post is table name and we need to define the keys or table columns
# to see sql query we will use below command
# python manage.py  sqlmigrate app_name migration_number
# python manage.py sqlmigrate blog 0001
# python manage.py makemigrations  .. to apply the changes in the table ..even though data exist in the table
# python manage.py migrate .. then we will do migrate
# similar to python interactive shell , we have django interactive shell ..we can open  the same by using
# python manage.py shell

# class Post(models.Model):
#     title = models.CharField(max_length=100)
#     content = models.TextField()
#     date_posted = models.DateTimeField(default=timezone.now)
#     author  = models.ForeignKey(User, on_delete=models.CASCADE)

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    # auto_now=True means it will display the last modification date , we want to display the actual posted date ..so
    # we are going for default=timezone.now
    date_posted = models.DateTimeField(default=timezone.now)
    # on delete is flag , like if user is deleted we are deleting the posts from user.
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title