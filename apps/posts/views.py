from django.shortcuts import render, redirect
from .models import Post
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms
from django.contrib.auth.models import User
# Create your views here.


@login_required(login_url='/account/login/')
def view_all_posts(request):
    author = request.user
    posts = Post.objects.all().order_by('date')
    posts_by_user = posts.filter(author=author)

    context = {
        'posts_by_user': posts_by_user
    }
    print(context['posts_by_user'])

    return render(request, 'posts/view_all_posts.html', context)


def post_detail(request, slug):
    # return HttpResponse(slug)
    post = Post.objects.get(slug=slug)
    context = {
        'post':  post
    }

    return render(request, 'posts/post_detail.html', context)


@login_required(login_url='/account/login/')
def post_edit(request, slug):
    # return HttpResponse(slug)
    post = Post.objects.get(slug=slug)
    form = forms.CreatePost(instance=post)

    if request.method == 'POST':
        form = forms.CreatePost(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('/posts/')

    context = {
        'form':  form,
        'post': post,
    }

    return render(request, 'posts/post_edit.html', context)


@login_required(login_url='/account/login/')
def post_create(request):
    if request.method == 'POST':
        form = forms.CreatePost(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('posts:list')

    else:
        form = forms.CreatePost()

    context = {
        'form': form
    }

    return render(request, 'posts/post_create.html', context)
