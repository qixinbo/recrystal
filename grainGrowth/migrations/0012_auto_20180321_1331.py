# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grainGrowth', '0011_auto_20180307_0700'),
    ]

    operations = [
        migrations.AlterField(
            model_name='executioner',
            name='dt',
            field=models.FloatField(default=25, verbose_name=b'time step'),
        ),
        migrations.AlterField(
            model_name='executioner',
            name='nl_rel_tol',
            field=models.FloatField(default=1e-10, verbose_name=b'relative tol for nonlinear solver'),
        ),
        migrations.AlterField(
            model_name='ic',
            name='grain_num',
            field=models.IntegerField(default=100, verbose_name=b'number of grains'),
        ),
        migrations.AlterField(
            model_name='ic',
            name='op_num',
            field=models.IntegerField(default=8, verbose_name=b'number of order paramaters'),
        ),
        migrations.AlterField(
            model_name='mesh',
            name='nx',
            field=models.IntegerField(default=11, verbose_name=b'No. of elements in x'),
        ),
        migrations.AlterField(
            model_name='mesh',
            name='ny',
            field=models.IntegerField(default=11, verbose_name=b'No. of elements in y'),
        ),
        migrations.AlterField(
            model_name='mesh',
            name='uniform_refine',
            field=models.IntegerField(default=3, verbose_name=b'initial uniform refinement'),
        ),
    ]
