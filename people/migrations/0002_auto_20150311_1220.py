from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='github_username',
            field=models.CharField(help_text=b'GitHub kullan\xc4\xb1c\xc4\xb1 ad\xc4\xb1n\xc4\xb1z\xc4\xb1 giriniz.', max_length=255, null=True, verbose_name=b'GitHub', blank=True),
            preserve_default=True,
        ),
    ]
