from django.shortcuts import render
from .models import Post
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms
# Create your views here.


def view_all_posts(request):
    posts = Post.objects.all().order_by('date')

    context = {
        'posts': posts
    }

    return render(request, 'posts/view_all_posts.html', context)


def post_detail(request, slug):
    # return HttpResponse(slug)
    post = Post.objects.get(slug=slug)
    context = {
        'post':  post
    }

    return render(request, 'posts/post_detail.html', context)


@login_required(login_url='/account/login/')
def post_create(request):
    if request.method == 'POST':
        form = forms.CreatePost(request.POST, request.FILES)
        if form.is_valid():
            return redirect('posts:list')

    else:
        form = forms.CreatePost()

    context = {
        'form': form
    }

    return render(request, 'posts/post_create.html')
