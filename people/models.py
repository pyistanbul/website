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
    is_active = models.BooleanField(default=True)

    objects = PeopleManager()

    class Meta:
        verbose_name_plural = "People"

    def __str__(self):
        return smart_text(self.name)

    def badge(self):
        if codecs.encode(self.email, "rot13") == "uhfrlvanyo@tznvy.pbz":
            return "huseyinalbing"


@python_2_unicode_compatible
class SocialAccountLink(models.Model):
    TWITTER = 'twitter'
    BLOG = 'home'
    GITHUB = 'github'

    ACCOUNT_TYPE_CHOICES = (
        (TWITTER, 'Twitter'),
        (BLOG, 'Blog'),
        (GITHUB, 'Github')
    )
    account_type = models.CharField(choices=ACCOUNT_TYPE_CHOICES,
                                    max_length=10)
    link = models.URLField(max_length=255)
    user = models.ForeignKey('auth.User', related_name='links')

    def __str__(self):
        return self.get_account_type_display()

    class Meta:
        unique_together = ('account_type', 'user',)
