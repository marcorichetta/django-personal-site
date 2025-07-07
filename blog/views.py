from django.shortcuts import render
from .models import Post


def home(request):
    posts = Post.objects.filter().all()
    return render(request, "blog/index.html", {"posts": posts})


def post(request, year, slug):
    post = Post.objects.get(year=year, slug=slug)
    return render(request, "post.html", {"post": post})
