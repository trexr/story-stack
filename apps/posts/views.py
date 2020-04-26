from django.shortcuts import render, redirect
from .models import Post
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms
from django.contrib.auth.models import User
# Create your views here.


@login_required(login_url='/account/login/')
def view_all_users_posts(request):
    # author = request.user
    authorid = request.user.id

    # posts = Post.objects.filter(deleted=False).order_by('date')
    # posts_by_user = posts.filter(author=author)

    context = {
        # 'posts_by_user': posts_by_user,
        'authorid': authorid
    }
    # print(author.id)

    return render(request, 'posts/view_all_users_posts.html', context)


@login_required(login_url='/account/login/')
def view_all_posts(request, id):
    author = request.user
    authorid = request.user.id

    posts = Post.objects.filter(deleted=False).order_by('date')
    posts_by_user = posts.filter(author=author)

    context = {
        'posts_by_user': posts_by_user,
        'authorid': authorid
    }
    print(author.id)

    return render(request, 'posts/view_all_posts.html', context)


def post_detail(request, slug, id):
    # return HttpResponse(slug)
    post = Post.objects.get(slug=slug)
    if post.deleted == True:
        return redirect('/403/')

    context = {
        'post':  post
    }

    return render(request, 'posts/post_detail.html', context)


@login_required(login_url='/account/login/')
def post_edit(request, slug, id):
    # return HttpResponse(slug)
    post = Post.objects.get(slug=slug)

    form = forms.CreatePost(instance=post)

    if post.deleted == True:
        return redirect('/403/')

    if request.method == 'POST':
        form = forms.CreatePost(request.POST, instance=post)
        if form.is_valid():
            instance = form.save(commit=False)
            print(request.POST)
            if 'Delete' in request.POST:
                instance.deleted = True
            instance.save()
            return redirect('posts:user_list', id=id)

    context = {
        'form':  form,
        'post': post,
    }

    return render(request, 'posts/post_edit.html', context)


@login_required(login_url='/account/login/')
def post_create(request, id):
    userid = request.user
    if request.method == 'POST':
        form = forms.CreatePost(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = userid
            instance.save()
            return redirect('posts:user_list', id=userid)

    else:
        form = forms.CreatePost()

    context = {
        'form': form,
        'userid': userid
    }

    return render(request, 'posts/post_create.html', context)
