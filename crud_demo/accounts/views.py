from django.shortcuts import render, redirect
from accounts.forms import RegistrationForm


def base(request):
    return render(request, 'base.html')


def home(request):
    return render(request, 'accounts/home.html')


def login(request):
    return render(request, 'accounts/login.html')


def login_redirect(request):
    return render(request, 'accounts/login.html')


def register(request):
    if request.method.lower() == 'post':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog_home')
    else:
        form = RegistrationForm()

    context = {'form': form}
    return render(request, 'accounts/register_user.html', context)
