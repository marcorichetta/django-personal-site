from blog import views
from django.urls import path

from .feed import BlogFeed

urlpatterns = [
    path("", views.home, name="blog_index"),
    path("feed/", BlogFeed()),
    path("<int:year>/<slug:slug>/", views.post, name="post"),
]
