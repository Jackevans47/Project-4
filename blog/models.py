from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date


# catagories
class Category(models.Model):
    name = models.CharField(max_length=255, default="uncategorised")

    def __str__(self):
        """Display name"""
        return self.name

    def get_absolute_url(self):
        """Directs url to add home"""
        return reverse("home")


# Create blog posts
class Post(models.Model):
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=255, default="F1 blog")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    post_date = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=255, default="uncategorised")

    def __str__(self):
        """Display title and user of blog post on page"""
        return self.title + " | " + str(self.author)

    def get_absolute_url(self):
        """Directs url to add post"""
        return reverse("article-details", args=[self.id])


# Comments on blog posts
class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    body = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)


# Like functionality on blog posts
class Like:
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
