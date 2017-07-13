from django.db import models
from django.utils.encoding import smart_text, python_2_unicode_compatible


@python_2_unicode_compatible
class Presentation(models.Model):
    title = models.CharField(max_length=255)
    owner = models.CharField(max_length=255)
    date = models.DateField()
    link = models.URLField(blank=True, null=True)
    description = models.TextField(blank=True)
    user = models.ForeignKey('auth.User', null=True, blank=True,
                             related_name='presentations')

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return smart_text(self.title)
