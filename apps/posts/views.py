from django.shortcuts import render, redirect
from .models import Post
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.validators import validate_email
import os
import requests
from django.conf import settings


# TODO: implement a view all friends posting feed
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

    # return redirect('posts:user_list', id=authorid)
    return render(request, 'posts/view_all_users_posts.html', context)


@login_required(login_url='/account/login/')
def view_all_posts(request, id):
    author = request.user
    authorid = request.user.id

    posts = Post.objects.filter(deleted=False).order_by('-date')
    posts_by_user = posts.filter(author=author)

    context = {
        'posts_by_user': posts_by_user,
        'authorid': authorid
    }
    print(author.id)

    return render(request, 'posts/view_all_posts.html', context)


def post_detail(request, slug, id):

    if request.method == 'POST':
        form = forms.EmailForm(request.POST)
        # Send Mailgun email
        if form.is_valid():
            # Get email from form
            email = form.cleaned_data['email']
            # Define variables for email information
            user_email = request.user.email
            title = Post.objects.get(slug=slug)
            story_title = str(title)
            authorid = request.user.id
            story_slug = str(slug)
            post_url = "http://" + request.get_host() + "/posts/" + \
                str(authorid) + "/" + story_slug
            print(post_url)
            requests.post(
                "https://api.mailgun.net/v3/sandboxba7fef7146b9468892448dede05c27cf.mailgun.org/messages",
                auth=("api", settings.MAILGUN_API_KEY),
                data={"from": "StoryStack <user@storystack.com>",
                              "to": email,
                              "subject": user_email+" wants to share a story with you!",
                      "text": "Check out my story '" + story_title + "' on StoryStack: "+post_url})

            print("email sent to", email)

            messages.success(request, 'Email Sent')
            return redirect("posts:view_user_post", id=id, slug=slug)

    else:
        form = forms.EmailForm()

    post = Post.objects.get(author_id=id, slug=slug)

    if post.deleted == True:
        return redirect("posts:user_list", id=id)

    context = {
        'post':  post,
        'form': form,
    }

    return render(request, 'posts/post_detail.html', context)


@login_required(login_url='/account/login/')
def post_edit(request, slug, id):

    post = Post.objects.get(author_id=id, slug=slug)

    form = forms.CreatePost(instance=post)
    print('form', post)
    if post.deleted == True:
        return redirect('/403/')

    if request.method == 'POST':
        form = forms.CreatePost(request.POST, request.FILES, instance=post)
        if form.is_valid():
            instance = form.save(commit=False)

            if 'Delete' in request.POST:
                instance.deleted = True
            instance.save()

            context = {
                'post':  instance,

            }

            return redirect("posts:view_user_post", id=instance.author_id, slug=instance.slug)

    context = {
        'form':  form,
        'post': post,
    }

    return render(request, 'posts/post_edit.html', context)


@login_required(login_url='/account/login/')
def post_create(request, id):

    if request.method == 'POST':
        form = forms.CreatePost(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('posts:user_list', id=request.user.id)

    else:
        form = forms.CreatePost()

    context = {
        'form': form,
        'userid': request.user.id
    }

    return render(request, 'posts/post_create.html', context)
