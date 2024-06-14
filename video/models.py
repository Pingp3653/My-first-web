from django.db import models
from embed_video.fields import EmbedVideoField
from django.utils.text import slugify
from django.contrib.auth.models import *
from taggit.managers import TaggableManager

class Youtube(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=100)
    video_url = EmbedVideoField(null=True, blank=True)
    description = models.TextField(max_length=280, null=True, blank=True)
    body = models.TextField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    date_updated = models.DateTimeField(auto_now=True, null=True, blank=True)
    slug = models.SlugField(unique=True, max_length=100, null=True, blank=True)
    tags = TaggableManager()

    def __str__(self):
        return self.title
    