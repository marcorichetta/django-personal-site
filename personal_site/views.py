from django.shortcuts import render

from blog.models import Post


def home(request):
    # Get the 3 most recent published blog posts
    recent_posts = Post.objects.filter(published=True).order_by("-created_at")[:3]
    return render(request, "home.html", {"recent_posts": recent_posts})


def home2(request):
    # Get the 3 most recent published blog posts
    recent_posts = Post.objects.filter(published=True).order_by("-created_at")[:3]
    return render(request, "home2.html", {"recent_posts": recent_posts})


def about(request):
    return render(request, "about.html")
