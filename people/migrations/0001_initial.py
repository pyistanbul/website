# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name=b'Ad ve Soyad')),
                ('email', models.EmailField(help_text=b'Gravatar i\xc3\xa7in gerekmektedir, sitede g\xc3\xb6z\xc3\xbckmeyecektir.', max_length=255)),
                ('blog_link', models.URLField(max_length=255, verbose_name=b'Blog URL')),
                ('twitter_username', models.CharField(help_text=b'Twitter kullan\xc4\xb1c\xc4\xb1 ad\xc4\xb1n\xc4\xb1z\xc4\xb1 giriniz.', max_length=255, null=True, verbose_name=b'Twitter', blank=True)),
                ('github_username', models.CharField(help_text=b'Github.com kullan\xc4\xb1c\xc4\xb1 ad\xc4\xb1n\xc4\xb1z\xc4\xb1 giriniz.', max_length=255, null=True, verbose_name=b'Github', blank=True)),
                ('is_active', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': 'People',
            },
            bases=(models.Model,),
        ),
    ]
