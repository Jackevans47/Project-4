from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from blog.models import Post
from .forms import FormPost, EditForm
from django.urls import reverse_lazy


# post blog post on main page
class Home(ListView):
    model = Post
    template_name = "home.html"
    ordering = ["-id"]


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


# delete post
class DeletePost(DeleteView):
    model = Post
    template_name = "delete_post.html"
    success_url = reverse_lazy("home")
