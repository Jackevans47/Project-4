from django.shortcuts import render
from django.views.generic import ListView, DetailView
from blog.models import Post


class Home(ListView):
    model = Post
    template_name = "home.html"


class Article(DetailView):
    model = Post
    template_name = "article.html"
