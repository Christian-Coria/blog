from django import forms

from .models import Comments, Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ("status", "created_on", "updated_on")

        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "slug": forms.TextInput(attrs={"class": "form-control"}),
            "content": forms.Textarea(attrs={"class": "form-control content"}),
            "image": forms.FileInput(attrs={"class": "form-control"}),
            "author": forms.HiddenInput(),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = (
            "post",
            "author",
            "text",
        )

        widgets = {
            "post": forms.HiddenInput(),
            "author": forms.HiddenInput(),
            "text": forms.Textarea(attrs={"class": "form-control content"}),
        }