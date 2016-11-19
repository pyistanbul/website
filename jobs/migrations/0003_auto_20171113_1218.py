# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_auto_20150311_1220'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='is_expired',
            field=models.BooleanField(default=False, verbose_name=b'S\xc3\xbcresi doldu'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='job',
            name='date_created',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name=b'Olu\xc5\x9fturulma Tarihi'),
            preserve_default=True,
        ),
    ]
