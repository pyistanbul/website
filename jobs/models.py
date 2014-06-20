# coding=utf-8
from django.db import models
from django.utils.encoding import smart_unicode
from django.utils.timezone import now

from markitup.fields import MarkupField

from .managers import JobsManager


class Job(models.Model):
    title = models.CharField(max_length=255, verbose_name='Başlık')
    company = models.CharField(max_length=255, verbose_name='Şirket Adı')
    url = models.URLField(max_length=255, verbose_name='Başvuru Linki')
    description = MarkupField(verbose_name='Açıklama',
                              help_text="Markdown formatında yazabilirsiniz.")
    location = models.CharField(max_length=255, verbose_name='Lokasyon')
    date_created = models.DateTimeField(default=now)

    objects = JobsManager()

    class Meta:
        ordering = ["-date_created"]

    @models.permalink
    def get_absolute_url(self):
        return 'jobs:detail', [self.pk]

    def __unicode__(self):
        return smart_unicode(self.title)
