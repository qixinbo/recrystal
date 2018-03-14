# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grainGrowth', '0010_auto_20180307_0313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='outputs',
            name='csv',
            field=models.CharField(default=b'true', max_length=5, verbose_name=b'csv file is exported?', choices=[(b'true', b'true'), (b'false', b'false')]),
        ),
    ]
