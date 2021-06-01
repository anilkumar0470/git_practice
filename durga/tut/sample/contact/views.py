from django.shortcuts import render, redirect
from .forms import ContactForm
# Create your views here.


def contactus(request):

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            return redirect('junk-details')
    else:
            form = ContactForm()
    return render(request, 'contact/hello.html', {'form': form})