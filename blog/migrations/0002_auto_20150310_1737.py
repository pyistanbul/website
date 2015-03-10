# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.management import call_command
from django.db import models, migrations


def load_fixture(apps, schema_editor):
    call_command('loaddata', 'radpress_posts')


def generate_html(apps, schema_editor):
    # Hack: Django fixture'ları import ederken modelin save()
    # metodunu çağırmadığından böyle bir maymunluk yapmak gerekiyor.
    Post = apps.get_model('blog', 'Post')
    for post in Post.objects.all():
        post.save()


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(load_fixture),
        migrations.RunPython(generate_html),
    ]
