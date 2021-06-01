from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            return HttpResponse("<div>Account has been created for this user: {{ username }}</div>")
    else:
        form = UserCreationForm()
    return render(request, 'users/new_register.html', {'form':form})





