from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.contrib.auth.models import User
from .forms import UserRegisterForm


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        print("34334343")
        if form.is_valid():

            form.save()
            return redirect('show-users')
        if form.errors:
            return HttpResponse(form.errors)

    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


def display_available_users(request):
    qs = User.objects.all()
    return render(request, 'users/display_all_users.html', {"var": qs})

