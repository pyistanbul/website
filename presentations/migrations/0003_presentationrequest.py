# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('presentations', '0002_auto_20170713_2300'),
    ]

    operations = [
        migrations.CreateModel(
            name='PresentationRequest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('presenter_name', models.CharField(max_length=255, verbose_name=b'Ad, Soyad')),
                ('presenter_email', models.EmailField(max_length=75, verbose_name=b'E-Mail')),
                ('presenter_twitter_username', models.CharField(max_length=255, verbose_name=b'Twitter kullanici adi')),
                ('presenter_github_username', models.CharField(max_length=255, verbose_name=b'Github kullanici adi')),
                ('presentation_title', models.CharField(max_length=255, verbose_name=b'Sunum Basligi')),
                ('presentation_type', models.CharField(max_length=255, verbose_name=b'Sunum Turu', choices=[(b'sunum', b'Sunum'), (b'workshop', b'Workshop'), (b'lightning-talk', b'Lightning Talk'), (b'soru-cevap', b'Soru & Cevap')])),
                ('presentation_duration', models.SmallIntegerField(help_text=b'dakika cinsinden', verbose_name=b'Tahmini Sure')),
                ('presentation_content', models.TextField(verbose_name=b'Sunum Icerigi')),
                ('application_date', models.DateField(auto_now_add=True)),
                ('is_approved', models.BooleanField(default=False, verbose_name=b'Begenildi')),
                ('is_reviewed', models.BooleanField(default=False, verbose_name=b'Degerlendirildi')),
            ],
            options={
                'ordering': ('-application_date',),
            },
            bases=(models.Model,),
        ),
    ]
