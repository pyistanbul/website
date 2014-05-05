# coding=utf-8
from django.db import models
from django.utils.encoding import smart_unicode


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
    is_active = models.BooleanField()

    class Meta:
        verbose_name_plural = "People"

    def __unicode__(self):
        return smart_unicode(self.name)

    def badge(self):
        if self.email.encode("rot13") == "uhfrlvanyo@tznvy.pbz":
            return "huseyinalbing"
