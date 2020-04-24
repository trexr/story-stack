from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=142)
    slug = models.CharField(max_length=225)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    #add in thumbnail and author
    # add in

    def __str__(self):
        return self.title
