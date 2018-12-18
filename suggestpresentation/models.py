from django.db import models

# Create your models here.

class suggest(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name='Ad ve Soyad')
    email = models.EmailField(
        max_length=255,)
    content = models.TextField(verbose_name="Öneriniz")

    class Meta:
        verbose_name_plural = "Suggestions"

    def __str__(self):
        return self.content

