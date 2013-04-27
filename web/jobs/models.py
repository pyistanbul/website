# coding=utf-8
from django.db import models
from django.utils.encoding import smart_unicode


class Job(models.Model):
    title = models.CharField(max_length=255, verbose_name='Başlık')
    company = models.CharField(max_length=255, verbose_name='Şirket Adı')
    url = models.URLField(max_length=255, verbose_name='Başvuru Linki')
    description = models.TextField(verbose_name='Açıklama')
    location = models.CharField(max_length=255, verbose_name='Lokasyon')

    def __unicode__(self):
        return smart_unicode(self.name)
