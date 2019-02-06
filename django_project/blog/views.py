from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'Swadhi',
        'title': 'Blog post 1',
        'content': 'First post content',
        'date_posted': '3, February 2019'
    },
    {
        'author': 'Dilip',
        'title': 'Blog post 2',
        'content': 'Second post content',
        'date_posted': '4, February 2019'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
