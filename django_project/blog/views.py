from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
# Create your views here.
from .models import Post


def home(request):
    context = {
        "posts": Post.objects.all()
    }
    return render(request,"blog/home.html", context)


def about(request):
    return render(request, "blog/about.html", {"title": "About"})

# django-admin startproject <project_name>
# python manage.py startapp <app_name>
# make sure that our apps are added in settings.py in installed_apps


# here we are using normal html tags . In real time we will have normal html files we cannot copy and paste the entire
# code here . instead of this we will use templates concept.
# create a folder called templates under blog(generally under app)
# inside templates folder create a folder called blog(generally app name) so that djano can look into this folder
# while running this app

# blog -->templates --> blog --> templates.html
# we need to add our app to installed apps as we are using templates
# go settings.py and add app details
# load the template , render the same as HttpResponse
# instead above one we will use render in the django.shortcuts .. so that we can render directly
# render function takes three arguments, request, html file path and context we will same in the coming time.
# path we need to appname followed by file name eg: blog/home.html
# now we are having static html ..lets see how to use variables in html we will use jinja2 template for the same
# we will use context variable to send the data from views which we got from data base to html file
# we can send data directly ..no need use context also


# if we see here we have two dis advantages
# writing the same code
# if i want to modify any code we have to modify in both files example title. To avoid the same we will use concept
# called template inheritance
# we will create html file and we will move the all common code to that html generally it will be base.html

# extends blog/base.html to inheritance the common html
# static folder for javascript or css files and inside we need to create folder with app name

# if we see html we are hard coding the routes
# instead of we need to use urls dynamically by using name tag given in urls.py
# syntax is {% url name tag value %} --> {% url 'blog-home' %}

# admin page
# when we route to admin it will ask username and password , however we dont have the same
# we will set the same through the terminal and then we will login
# python manage.py createsuperuser
# after executing the above command we will hit the error like not table
# to avoid the same we will use migrations
# python manage.py makemigrations -- prepare will everything
# python manage.py migrate -- execution will be done here
# python manage.py createsuperuser
# username/password : test/test
# staff status means whether he can login to admin page or not
# superuserstatus means root user ..so that he can delete or add user

# object relation mapper
# we can use multiple data bases at the same
# we can use one data base for testing and another data base for production as the queries are handled by orm
# we will represent the data base structure as class in ORM
# with in the app, django will create models.py we will work on the same.
# to see the sql query backend it used to create the table
# python manage.py sqlmigrate <appname> <querynumber--after execuitng makemigrations we ill get one sequence number>
# python manage.py sqlmigrate blog 0001
