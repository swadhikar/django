from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import CreatePostForm, UpdatePostForm
from .models import Post


def index(request):
    posts = Post.objects.all()
    context = {'posts': posts[::-1]}
    return render(request, 'blog/blog_home.html', context=context)


@login_required
def create_post(request):
    if request.method == 'POST':
        form = CreatePostForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('blog_home')
    else:
        form = CreatePostForm()

    context = {'form': form}
    return render(request, 'blog/blog_create.html', context=context)


@login_required
def delete_post(request, id):
    Post.objects.get(pk=id).delete()
    return redirect('blog_home')


@login_required
def update_post(request, id):
    post = Post.objects.get(pk=id)
    form = UpdatePostForm(request.POST or None, instance=post)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('blog_home')
    context = {'form': form}
    return render(request, 'blog/blog_update.html', context=context)
