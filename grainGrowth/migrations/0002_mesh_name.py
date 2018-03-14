# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grainGrowth', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mesh',
            name='name',
            field=models.CharField(default=b'test 1', max_length=20, verbose_name=b'Mesh Name'),
        ),
    ]
