# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grainGrowth', '0005_auto_20180305_0721'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mesh',
            name='nx',
            field=models.IntegerField(default=10, verbose_name=b'No. of elements in x'),
        ),
        migrations.AlterField(
            model_name='mesh',
            name='ny',
            field=models.IntegerField(default=10, verbose_name=b'No. of elements in y'),
        ),
        migrations.AlterField(
            model_name='mesh',
            name='nz',
            field=models.IntegerField(default=0, verbose_name=b'No. of elements in z'),
        ),
    ]
