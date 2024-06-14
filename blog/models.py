from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import *
from taggit.managers import TaggableManager

class Author(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="author-image/", null=True,blank=True,default='default.png')
    
    def __str__(self):
        return self.name


class Post(models.Model):
    author = models. ForeignKey(Author, on_delete=models.CASCADE, null=True, blank=True)
    title = models. CharField(max_length=200)
    description = models. TextField(max_length=280, null=True, blank=True)
    body = models.TextField(null=True, blank=True)
    images = models. ImageField(upload_to="post-images/", null=True, blank=True)
    date_created = models. DateTimeField(auto_now_add=True, null=True, blank=True)
    date_updated = models. DateTimeField(auto_now=True)
    slug = models. SlugField(unique=True, max_length=180, null=True, blank=True)
    tags = TaggableManager()


def _str_(self):
    return self.title   
