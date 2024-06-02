from django.urls import path
from .views import (
    Home,
    Article,
    AddPost,
    EditPost,
    DeletePost,
    AddCategory,
    CategoryView,
)

urlpatterns = [
    path("", Home.as_view(), name="home"),
    path("article/<int:pk>", Article.as_view(), name="article-details"),
    path("add_post/", AddPost.as_view(), name="add_post"),
    path("add_category/", AddCategory.as_view(), name="add_category"),
    path("article/edit/<int:pk>", EditPost.as_view(), name="edit_post"),
    path("article/<int:pk>/delete", DeletePost.as_view(), name="delete_post"),
    path("category/<str:cats>/", CategoryView, name="category"),
]
