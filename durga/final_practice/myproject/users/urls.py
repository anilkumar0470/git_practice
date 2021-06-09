from django.shortcuts import render
from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.register, name='register'),
    path('user_details/', views.display_available_users, name='show-users')
]