from django.db import models


class Presentation(models.Model):
    title = models.CharField(max_length=255)
    owner = models.CharField(max_length=255)
    date = models.DateField()
    link = models.URLField(blank=True, null=True)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.title
