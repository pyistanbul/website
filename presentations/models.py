from django.db import models
from django.utils.encoding import smart_text, python_2_unicode_compatible


@python_2_unicode_compatible
class Presentation(models.Model):
    title = models.CharField(max_length=255)
    owner = models.CharField(max_length=255)
    date = models.DateField()
    link = models.URLField(blank=True, null=True)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return smart_text(self.title)


class PresentationRequest(models.Model):
    presentation_type_choices = (
        ('sunum', "Sunum"),
        ('workshop', "Workshop"),
        ('lightning-talk', "Lightning Talk"),
        ('soru-cevap', "Soru & Cevap"),
    )

    presenter_name = models.CharField(verbose_name='Ad, Soyad', max_length=255)
    presenter_email = models.EmailField(verbose_name='E-Mail')
    presenter_twitter_username = models.CharField(verbose_name='Twitter kullanici adi', max_length=255)
    presenter_github_username = models.CharField(verbose_name='Github kullanici adi', max_length=255)
    presentation_title = models.CharField(verbose_name='Sunum Basligi', max_length=255)
    presentation_type = models.CharField(verbose_name='Sunum Turu',choices=presentation_type_choices, max_length=255)
    presentation_duration = models.SmallIntegerField(verbose_name='Tahmini Sure', help_text='dakika')
    presentation_content = models.TextField(verbose_name='Sunum Icerigi')
    application_date = models.DateField(auto_now_add=True)
    is_approved = models.BooleanField(verbose_name='Begenildi', default=False)
    is_reviewed = models.BooleanField(verbose_name='Degerlendirildi', default=False)

    class Meta:
        ordering = ('-application_date', )

    def __str__(self):
        return smart_text("{}, {}".format(self.presentation_title, self.name))
