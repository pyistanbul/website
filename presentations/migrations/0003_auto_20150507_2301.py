# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('presentations', '0002_presentation_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='presentation',
            name='user',
            field=models.ForeignKey(related_name='presentations', blank=True, to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
    ]
