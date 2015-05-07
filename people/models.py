# coding=utf-8
from django.db import models
from django.utils.encoding import smart_unicode
from .managers import PeopleManager


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
        max_length=255, blank=True, null=True, verbose_name='Github',
        help_text='Github.com kullanıcı adınızı giriniz.')
    is_active = models.BooleanField(default=False)

    objects = PeopleManager()

    class Meta:
        verbose_name_plural = "People"

    def __unicode__(self):
        return smart_unicode(self.name)

    def badge(self):
        if self.email.encode("rot13") == "uhfrlvanyo@tznvy.pbz":
            return "huseyinalbing"


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

    def __unicode__(self):
        return '%s - %s' % (self.get_account_type_display(), self.user)

    class Meta:
        unique_together = ('account_type', 'user',)
