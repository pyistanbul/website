from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0002_auto_20150311_1220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='is_active',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]
