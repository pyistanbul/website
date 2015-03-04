# coding=utf-8
from django.db import models
from django.utils.encoding import smart_unicode

from markitup.fields import MarkupField
from .managers import BlogManager


class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    description = MarkupField()
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    is_published = models.BooleanField(default=True)

    objects = BlogManager()

    class Meta:
        ordering = ["-created_at"]

    def __unicode__(self):
        return smart_unicode(self.title)

    @models.permalink
    def get_absolute_url(self):
        return 'blog:blog-detail', [self.slug]
