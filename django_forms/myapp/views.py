from django.shortcuts import render
from .forms import (
    ContactForm,
    SnippetForm
)


# Create your views here.
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']

    else:
        form = ContactForm()

    return render(request, 'form.html', {'form': form})


def snippet_details(request):
    if request.method == 'POST':
        form = SnippetForm(request.POST)

        if form.is_valid():
            form.save()

    else:
        form = SnippetForm()

    return render(request, 'form.html', {'form': form})
