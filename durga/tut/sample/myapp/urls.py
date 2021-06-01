from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.display_details, name='junk-details'),
]
