from django.urls import path
from django.urls import include
from .views import student_details

urlpatterns = [
    path('display/', student_details, name='display_details'),
]
