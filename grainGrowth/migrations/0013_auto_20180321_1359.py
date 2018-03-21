# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grainGrowth', '0012_auto_20180321_1331'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='executioner',
            name='nl_abs_tol',
        ),
        migrations.RemoveField(
            model_name='executioner',
            name='nl_rel_tol',
        ),
    ]
