from django.shortcuts import render, redirect
from .models import Post
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms
from django.contrib.auth.models import User
from django.core.validators import validate_email
import os
import requests
mailgun_api_key = os.environ["MAILGUN_API_KEY"]
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

    # return redirect('posts:user_list', id=authorid)
    # TODO: may want to create feed with friends stories
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
            first_name = request.user.first_name
            post = Post.objects.get(slug=slug)
            title = str(post)
            url_title = title.replace(" ", "-")
            authorid = request.user.id
            post_url = "http://localhost:8000/posts/" + \
                str(authorid) + "/" + url_title
            requests.post(
                "https://api.mailgun.net/v3/sandboxba7fef7146b9468892448dede05c27cf.mailgun.org/messages",
                auth=("api", mailgun_api_key),
                data={"from": "StoryStack <user@storystack.com>",
                              "to": email,
                              "subject": first_name+" wants to share a story with you!",
                      "text": "Check out my story '" + str(post) + "' on StoryStack: "+post_url})

            print("email sent", email, )
            return redirect("posts:view_user_post", id=id, slug=slug)

    else:
        form = forms.EmailForm()

    # return HttpResponse(slug)
    post = Post.objects.get(slug=slug)

    if post.deleted == True:
        return redirect('/403/')

    context = {
        'post':  post,
        'form': form,
    }

    return render(request, 'posts/post_detail.html', context)


@login_required(login_url='/account/login/')
def post_edit(request, slug, id):
    # return HttpResponse(slug)
    post = Post.objects.get(slug=slug)

    form = forms.CreatePost(instance=post)
    print('form', post)
    if post.deleted == True:
        return redirect('/403/')

    if request.method == 'POST':
        form = forms.CreatePost(request.POST, request.FILES, instance=post)
        if form.is_valid():
            instance = form.save(commit=False)
            print(request.FILES)
            if 'Delete' in request.POST:
                instance.deleted = True
            instance.save()
            context = {
                'post':  post
            }
            return render(request, 'posts/post_detail.html', context)

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
