from django.urls import path
from django.urls import include
from . import views
urlpatterns = [
    path('contactme/', views.contactus, name='contact-me'),
]