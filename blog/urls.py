from django.urls import path, include
from .views import (
    Home,
    Article,
    AddPost,
    EditPost,
    DeletePost,
    AddCategory,
    CategoryView,
    CategoryListView,
)

urlpatterns = [
    path("", Home.as_view(), name="home"),
    path("article/<int:pk>", Article.as_view(), name="article-details"),
    path("add_post/", AddPost.as_view(), name="add_post"),
    path("add_category/", AddCategory.as_view(), name="add_category"),
    path("article/edit/<int:pk>", EditPost.as_view(), name="edit_post"),
    path("article/<int:pk>/delete", DeletePost.as_view(), name="delete_post"),
    path("category/<int:pk>/", CategoryView, name="category"),
    path("category-list/", CategoryListView, name="category-list"),
    path("<int:uid>/", include("members.urls")),
]
