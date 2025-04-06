from blog import views
from django.urls import path

from .feed import BlogFeed

urlpatterns = [
    path("", views.home, name="blog_index"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("blog/", views.blog, name="blog"),
    path("feed/", BlogFeed()),
]
