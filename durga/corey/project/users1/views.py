from django.shortcuts import render
from django.contri.auth.forms import UserCreationForm


def register(request):
    form = UserCreationForm()

    return render(request, "users1/register.html", {"form": form})
