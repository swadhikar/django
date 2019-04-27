from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from accounts.forms import RegistrationForm, HomeForm
from django.views.generic.base import TemplateView


def base(request):
    return render(request, 'base.html')


def home(request):
    # return render(request, 'accounts/home.html')
    return render(request, 'accounts/my_home.html')


def login(request):
    return render(request, 'accounts/login.html')


def login_redirect(request):
    return render(request, 'blog/blog_home.html')


def register(request):
    if request.method.lower() == 'post':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistrationForm()

    context = {'form': form}
    return render(request, 'accounts/register_user.html', context)


@login_required
def profile(request):
    context = {'user': request.user}
    return render(request, 'accounts/profile.html', context=context)


class HomeView(TemplateView):
    template_name = 'accounts/my_home.html'

    def get(self, request):
        form = HomeForm()
        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request):
        text = 'None'
        form = HomeForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['post']
            form = HomeForm()
            # return redirect('home')

        context = {'form': form, 'text': text}
        return render(request, self.template_name, context)

