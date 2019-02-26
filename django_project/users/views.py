from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import (
    UserRegisterForm,
    UserUpdateForm,
    ProfileUpdateForm
)
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
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(
            request.POST,
            request.FILES,
            instance=request.user.profile
        )

        # Save forms
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Your account has been updated!' )
            return redirect('login')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'users/profile.html', context=context)
