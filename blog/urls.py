from django.urls import path
from .views import Home, Article, AddPost, EditPost

urlpatterns = [
    path("", Home.as_view(), name="home"),
    path("article/<int:pk>", Article.as_view(), name="article-details"),
    path("add_post/", AddPost.as_view(), name="add_post"),
    path("article/edit/<int:pk>", EditPost.as_view(), name="edit_post"),
]
