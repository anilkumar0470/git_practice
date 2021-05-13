from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect
from .forms import UserRegisterForm
from  django.contrib.auth.decorators import login_required
# messages.debug
# messages.info
# messages.success
# messages.warning
# messages.error


def register(request):

    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, "you account has been created and u r able to login now {}".format(username))
            return redirect('login')

    else:
        form = UserRegisterForm()

    return render(request, "users2/register.html", {'form': form})

@login_required
def profile(request):
    return render(request, 'users2/profile.html')

