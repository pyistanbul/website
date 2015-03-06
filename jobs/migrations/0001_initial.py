# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import markitup.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255, verbose_name=b'Ba\xc5\x9fl\xc4\xb1k')),
                ('company', models.CharField(max_length=255, verbose_name=b'\xc5\x9eirket Ad\xc4\xb1')),
                ('url', models.URLField(max_length=255, verbose_name=b'Ba\xc5\x9fvuru Linki')),
                ('description', markitup.fields.MarkupField(help_text=b'Markdown format\xc4\xb1nda yazabilirsiniz.', verbose_name=b'A\xc3\xa7\xc4\xb1klama')),
                ('location', models.CharField(max_length=255, verbose_name=b'Lokasyon')),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('_description_rendered', models.TextField(editable=False, blank=True)),
            ],
            options={
                'ordering': ['-date_created'],
            },
            bases=(models.Model,),
        ),
    ]
