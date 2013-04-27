from django.db import models
from django.utils.encoding import smart_unicode


class Person(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    blog_link = models.URLField(max_length=255)
    twitter_username = models.CharField(max_length=255)
    github_username = models.CharField(max_length=255)
    is_active = models.BooleanField()

    class Meta:
        verbose_name_plural = "People"

    def __unicode__(self):
        return smart_unicode(self.name)
