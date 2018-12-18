# coding: utf-8

from django.db import models
from django.utils.encoding import smart_text, python_2_unicode_compatible
from django.conf import settings

from markdownx.models import MarkdownxField
from markdownx.utils import markdownify

from .managers import BlogManager


@python_2_unicode_compatible
class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    description = MarkdownxField()
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    is_published = models.BooleanField(default=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    objects = BlogManager()

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return smart_text(self.title)

    @property
    def description_html(self):
        return markdownify(self.description)

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('blog:detail', args=[str(self.slug)])
