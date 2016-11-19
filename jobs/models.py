# coding: utf-8

from django.db import models
from django.utils.encoding import smart_text, python_2_unicode_compatible
from django.utils.timezone import now

from markitup.fields import MarkupField

from .managers import JobsManager


@python_2_unicode_compatible
class Job(models.Model):
    title = models.CharField(max_length=255, verbose_name='Başlık')
    company = models.CharField(max_length=255, verbose_name='Şirket Adı')
    location = models.CharField(max_length=255, verbose_name='Konum')
    is_expired = models.BooleanField(default=False, verbose_name='Süresi doldu')
    url = models.URLField(max_length=255, verbose_name='Başvuru Linki')
    description = MarkupField(verbose_name='Açıklama',
                              help_text="Markdown formatında yazabilirsiniz.")
    date_created = models.DateTimeField(default=now, verbose_name='Oluşturulma Tarihi')

    objects = JobsManager()

    class Meta:
        ordering = ["-date_created"]

    @models.permalink
    def get_absolute_url(self):
        return 'jobs:detail', [self.pk]

    def __str__(self):
        return smart_text(self.title)
