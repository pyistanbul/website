# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0002_socialaccountlink'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socialaccountlink',
            name='account_type',
            field=models.CharField(max_length=10, choices=[(b'twitter', b'Twitter'), (b'home', b'Blog'), (b'github', b'Github')]),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='socialaccountlink',
            unique_together=set([('account_type', 'user')]),
        ),
    ]
