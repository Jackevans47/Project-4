from django import forms
from .models import Post, Category

type = Category.objects.all().values_list("name", "name")

type_list = []

for item in type:
    type_list.append(item)


class FormPost(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title", "title_tag", "category", "body", "snippet")

        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "title_tag": forms.TextInput(attrs={"class": "form-control"}),
            # "author": forms.Select(attrs={"class": "form-control"}),
            "category": forms.Select(
                choices=type_list, attrs={"class": "form-control"}
            ),
            "body": forms.Textarea(attrs={"class": "form-control"}),
            "snippet": forms.Textarea(attrs={"class": "form-control"}),
        }


class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title", "title_tag", "body", "snippet")

        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "title_tag": forms.TextInput(attrs={"class": "form-control"}),
            # "author": forms.Select(attrs={"class": "form-control"}),
            "body": forms.Textarea(attrs={"class": "form-control"}),
            "snippet": forms.Textarea(attrs={"class": "form-control"}),
        }
