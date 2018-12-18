# coding: utf-8

from django.db import models
from django.utils.encoding import smart_text, python_2_unicode_compatible
from django.conf import settings

from markitup.fields import MarkupField

from .managers import BlogManager


@python_2_unicode_compatible
class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    description = MarkupField()
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    is_published = models.BooleanField(default=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    objects = BlogManager()

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return smart_text(self.title)

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('blog:detail', args=[str(self.slug)])
