from django.db import models
from django.utils.encoding import smart_unicode


class Presentation(models.Model):
    title = models.CharField(max_length=255)
    owner = models.CharField(max_length=255)
    date = models.DateField()
    link = models.URLField()
    description = models.TextField()

    class Meta:
        ordering = ['-date']

    def __unicode__(self):
        return smart_unicode(self.title)
