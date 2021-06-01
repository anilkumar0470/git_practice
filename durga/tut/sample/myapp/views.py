from django.shortcuts import render
from .models import DreamReal


def display_details(request):
    info = DreamReal.objects.all()
    return render(request, 'myapp/sample.html', {'all_info': info})
