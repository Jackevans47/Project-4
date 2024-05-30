from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from blog.models import Post


# post blog post on main page
class Home(ListView):
    model = Post
    template_name = "home.html"


# post one blog post on page
class Article(DetailView):
    model = Post
    template_name = "article.html"


# create posts
class AddPost(CreateView):
    model = Post
    template_name = "add_post.html"
    fields = "__all__"
