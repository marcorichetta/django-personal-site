from blog import views
from django.urls import path

urlpatterns = [
    path("", views.home, name="blog_index"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
]
