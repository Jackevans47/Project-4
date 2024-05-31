from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from blog.models import Post
from .forms import FormPost, EditForm


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
    form_class = FormPost
    template_name = "add_post.html"
    # fields = ("title", "body")


# edit posts
class EditPost(UpdateView):
    model = Post
    form_class = EditForm
    template_name = "edit_post.html"
    # fields = ["title", "title_tag", "body"]
