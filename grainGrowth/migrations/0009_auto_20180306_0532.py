# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grainGrowth', '0008_auto_20180306_0306'),
    ]

    operations = [
        migrations.AddField(
            model_name='executioner',
            name='l_max_its',
            field=models.IntegerField(default=30, verbose_name=b'max number of linear iter'),
        ),
        migrations.AddField(
            model_name='executioner',
            name='l_tol',
            field=models.FloatField(default=0.0001, verbose_name=b'relative tol for linear solver'),
        ),
        migrations.AddField(
            model_name='executioner',
            name='nl_abs_tol',
            field=models.FloatField(default=1e-11, verbose_name=b'absolute tol for nonlinear solver'),
        ),
        migrations.AddField(
            model_name='executioner',
            name='nl_max_its',
            field=models.IntegerField(default=40, verbose_name=b'max no. of nonlinear iters'),
        ),
        migrations.AddField(
            model_name='executioner',
            name='nl_rel_tol',
            field=models.FloatField(default=1e-08, verbose_name=b'relative tol for nonlinear solver'),
        ),
        migrations.AlterField(
            model_name='mesh',
            name='xmax',
            field=models.FloatField(default=1000, verbose_name=b'max x-coordinate'),
        ),
        migrations.AlterField(
            model_name='mesh',
            name='xmin',
            field=models.FloatField(default=0, verbose_name=b'min x-coordinate'),
        ),
        migrations.AlterField(
            model_name='mesh',
            name='ymax',
            field=models.FloatField(default=1000, verbose_name=b'max y-coordinate'),
        ),
        migrations.AlterField(
            model_name='mesh',
            name='ymin',
            field=models.FloatField(default=0, verbose_name=b'min y-coordinate'),
        ),
        migrations.AlterField(
            model_name='mesh',
            name='zmax',
            field=models.FloatField(default=0, verbose_name=b'max z-coordinate'),
        ),
        migrations.AlterField(
            model_name='mesh',
            name='zmin',
            field=models.FloatField(default=0, verbose_name=b'min z-coordinate'),
        ),
        migrations.AlterField(
            model_name='outputs',
            name='csv',
            field=models.CharField(default=b'true', max_length=5, verbose_name=b'csv file is exported?', choices=[(b'true', b'true'), (b'false', b'false')]),
        ),
        migrations.AlterField(
            model_name='outputs',
            name='exodus',
            field=models.CharField(default=b'true', max_length=5, verbose_name=b'exodus file is exported?', choices=[(b'true', b'true'), (b'false', b'false')]),
        ),
    ]
