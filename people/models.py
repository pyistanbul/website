# coding: utf-8

import codecs

from django.db import models
from django.utils.encoding import smart_text, python_2_unicode_compatible

from .managers import PeopleManager


@python_2_unicode_compatible
class Person(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name='Ad ve Soyad')
    email = models.EmailField(
        max_length=255,
        help_text='Gravatar için gerekmektedir, sitede gözükmeyecektir.')
    blog_link = models.URLField(max_length=255, verbose_name="Blog URL")
    twitter_username = models.CharField(
        max_length=255, blank=True,
        null=True, verbose_name='Twitter',
        help_text='Twitter kullanıcı adınızı giriniz.')
    github_username = models.CharField(
        max_length=255, blank=True, null=True, verbose_name='GitHub',
        help_text='GitHub kullanıcı adınızı giriniz.')
    is_active = models.BooleanField(default=False)

    objects = PeopleManager()

    class Meta:
        verbose_name_plural = "People"

    def __str__(self):
        return smart_text(self.name)

    def badge(self):
        if codecs.encode(self.email, "rot13") == "uhfrlvanyo@tznvy.pbz":
            return "huseyinalbing"
