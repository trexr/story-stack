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

# class MultiEmailField(forms.Field):
#    def to_python(self, value):
#        if not value:
#            return []
#        return value.split(',')

#    def validate(self, value):
#        super().validate(value)
#        for email in value:
#            validate_email(email)


class EmailForm(forms.Form):
    email = forms.EmailField()
