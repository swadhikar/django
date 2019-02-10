from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
    else:
        form = UserRegisterForm()

    if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        messages.success(request, 'Your account has been created! You can now be able to log in'.format(username))
        return redirect('login')

    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    return render(request, 'users/profile.html')
