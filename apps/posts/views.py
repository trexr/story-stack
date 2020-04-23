from django.shortcuts import render
from .models import Post
from django.http import HttpResponse
# Create your views here.


def view_all_posts(request):
    posts = Post.objects.all().order_by('date')

    context = {
        'posts': posts
    }

    return render(request, 'posts/view_all_posts.html', context)


def post_detail(request, slug):
    return HttpResponse(slug)
