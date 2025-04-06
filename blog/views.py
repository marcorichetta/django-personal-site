from django.shortcuts import render
from .models import Post

# Create your views here.


def home(request):
    posts = Post.objects.filter().all()
    print(posts)
    return render(request, "home.html", {"posts": posts})


def about(request):
    post = Post.objects.get(slug="about-me")
    if not post:
        return render(request, "404.html")

    return render(request, "about.html", {"post": post})


def contact(request):
    return render(request, "contact.html")


def blog(request):
    return render(request, "blog.html")
