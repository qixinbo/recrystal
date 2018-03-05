# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grainGrowth', '0002_mesh_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='materials',
            name='name',
            field=models.CharField(default=b'Cu', max_length=20, verbose_name=b'Material Name'),
        ),
    ]
