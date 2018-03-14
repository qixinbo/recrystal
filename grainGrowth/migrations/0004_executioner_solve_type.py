# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grainGrowth', '0003_materials_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='executioner',
            name='solve_type',
            field=models.CharField(default=b'PJFNK', max_length=20, verbose_name=b'Solver type'),
        ),
    ]
