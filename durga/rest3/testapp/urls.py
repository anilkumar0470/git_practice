from django.contrib import admin
from django.urls import path
from .views import blog_home
urlpatterns = [
    path('', blog_home, name="blog-name"),
]
