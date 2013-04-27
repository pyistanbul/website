from django.db import models
from django.utils.encoding import smart_unicode


class Company(models.Model):
    name = models.CharField(max_length=255)
    web_site = models.URLField()

    class Meta:
        verbose_name_plural = "Companies"

    def __unicode__(self):
        return smart_unicode(self.name)


class Job(models.Model):
    title = models.CharField(max_length=255)
    company = models.ForeignKey(Company, related_name="jobs")
    description = models.TextField()
    location = models.CharField(max_length=255)

    def __unicode__(self):
        return smart_unicode(self.name)
