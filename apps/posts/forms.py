from django import forms
from . import models


class CreatePost(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = ['title', 'body', 'storyimage']
        labels = {
            "body": "Story",
            "storyimage": "Art Image"
        }


class EmailForm(forms.Form):
    email = forms.EmailField()
