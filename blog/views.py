from django.shortcuts import render
from .models import Post

# Create your views here.


def index(request):
    posts = Post.objects.filter(published=True).all()

    return render(request, "index.html", {"posts": posts})


def about(request):
    return render(request, "about.html")


def contact(request):
    return render(request, "contact.html")


def blog(request):
    return render(request, "blog.html")
