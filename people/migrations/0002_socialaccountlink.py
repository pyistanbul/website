# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('people', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SocialAccountLink',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('account_type', models.CharField(max_length=10, choices=[(b'twitter', b'Twitter'), (b'blog', b'Blog'), (b'github', b'Github')])),
                ('link', models.URLField(max_length=255)),
                ('user', models.ForeignKey(related_name='links', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
