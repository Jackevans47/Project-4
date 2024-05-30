from django.urls import path
from .views import Home, Article, AddPost

urlpatterns = [
    path("", Home.as_view(), name="home"),
    path("article/<int:pk>", Article.as_view(), name="article-details"),
    path("add_post/", AddPost.as_view(), name="add_post"),
]
