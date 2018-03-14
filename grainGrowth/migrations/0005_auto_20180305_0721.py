# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grainGrowth', '0004_executioner_solve_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='executioner',
            name='solve_type',
            field=models.CharField(default=b'PJFNK', max_length=20, verbose_name=b'solver type'),
        ),
        migrations.AlterField(
            model_name='mesh',
            name='name',
            field=models.CharField(default=b'test 1', max_length=20, verbose_name=b'mesh name'),
        ),
        migrations.AlterField(
            model_name='mesh',
            name='nx',
            field=models.IntegerField(default=10, verbose_name=b'No. of Elements in x-direction'),
        ),
        migrations.AlterField(
            model_name='mesh',
            name='ny',
            field=models.IntegerField(default=10, verbose_name=b'No. of elements in y-direction'),
        ),
        migrations.AlterField(
            model_name='mesh',
            name='nz',
            field=models.IntegerField(default=0, verbose_name=b'No. of elements in z-direction'),
        ),
        migrations.AlterField(
            model_name='mesh',
            name='xmax',
            field=models.FloatField(default=1000, verbose_name=b'maximum x-coordinate'),
        ),
        migrations.AlterField(
            model_name='mesh',
            name='xmin',
            field=models.FloatField(default=0, verbose_name=b'minium x-coordinate'),
        ),
        migrations.AlterField(
            model_name='mesh',
            name='ymax',
            field=models.FloatField(default=1000, verbose_name=b'maximum y-coordinate'),
        ),
        migrations.AlterField(
            model_name='mesh',
            name='ymin',
            field=models.FloatField(default=0, verbose_name=b'minium y-coordinate'),
        ),
        migrations.AlterField(
            model_name='mesh',
            name='zmax',
            field=models.FloatField(default=0, verbose_name=b'maximum z-coordinate'),
        ),
        migrations.AlterField(
            model_name='mesh',
            name='zmin',
            field=models.FloatField(default=0, verbose_name=b'minium z-coordinate'),
        ),
    ]
