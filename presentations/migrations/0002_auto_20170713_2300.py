from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('presentations', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='presentation',
            name='link',
            field=models.URLField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
