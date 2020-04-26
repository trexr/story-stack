from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.utils.text import slugify

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=142)
    slug = models.CharField(max_length=225)
    body = models.TextField(blank=True)
    date = models.DateTimeField(auto_now_add=True)
    storyimage = models.ImageField(default='default.jpg')
    deleted = models.BooleanField(default=False)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.title

    # method for generating unique post urls - aka slugs
    def get_unique_slug(self):
        slug = slugify(self.title)
        unique_slug = slug
        num = 1
        while Post.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug

    # may need better solution than overriding save methond
    def save(self, *args, **kwargs):
        self.slug = self.get_unique_slug()
        super().save(*args, **kwargs)
