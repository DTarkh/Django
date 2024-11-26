from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from django.contrib.auth import logout



def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)

        if form.is_valid():
            user = form.save()
            return redirect( 'bookshop:index')

        else:
            return render(request, 'registration/registration.html', {'form': form})

    else:
        form = UserRegistrationForm()

        return render(request, 'registration/registration.html', {'form': form})


def Logout(request):
    logout(request)

    return redirect('bookshop:index')