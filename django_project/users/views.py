from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
    else:
        form = UserRegisterForm()

    if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        messages.success(request, 'Account created for {}!'.format(username))
        return redirect('blog-home')

    return render(request, 'users/register.html', {'form': form})
