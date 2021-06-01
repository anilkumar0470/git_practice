from django.shortcuts import render, redirect
from .form import ContactForm
# Create your views here.


def contactus(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            return redirect('display_details')
    else:
            form = ContactForm()

    return render(request, 'contact/contactus.html', {'form' : form})