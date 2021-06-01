from . import views
from django.urls import path, include

urlpatterns = [
    path('contactme/', views.contactus, name='contact-me'),
]
