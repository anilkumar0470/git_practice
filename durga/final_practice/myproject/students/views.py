from django.shortcuts import render
from .models import Student


def student_details(request):
    details = Student.objects.all()

    return render(request, 'students/display.html', {'form': details})

