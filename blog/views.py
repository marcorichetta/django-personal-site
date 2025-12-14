from django.shortcuts import render, get_object_or_404
from .models import Post


def home(request):
    posts = Post.objects.filter(published=True)
    return render(request, "blog/index.html", {"posts": posts})


def post(request, year, slug):
    post = get_object_or_404(Post, created_at__year=year, slug=slug, published=True)
    return render(request, "blog/post.html", {"post": post})
