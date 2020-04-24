from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=142)
    slug = models.CharField(max_length=225)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    storyimage = models.ImageField(default='default.jpg', blank=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.title
