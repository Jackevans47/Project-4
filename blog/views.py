from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from blog.models import Post, Category
from .forms import FormPost, EditForm
from django.urls import reverse_lazy


# post blog post on main page
class Home(ListView):
    model = Post
    template_name = "home.html"
    ordering = ["-timestamp"]

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(Home, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context


class AddPostView(CreateView):

    model = Post
    form_class = FormPost
    template_name = "add_post.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


def CategoryListView(request):
    cat_menu_list = Category.objects.all()
    return render(
        request, "category_list.html", {"cat_menu_list": cat_menu_list}
    )


def CategoryView(request, cats):
    category_posts = Post.objects.filter(category=cats)
    return render(
        request,
        "categories.html",
        {"cats": cats.title(), "category_posts": category_posts},
    )


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


# add category
class AddCategory(CreateView):
    model = Category
    # form_class = FormPost
    template_name = "add_category.html"
    fields = "__all__"


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
