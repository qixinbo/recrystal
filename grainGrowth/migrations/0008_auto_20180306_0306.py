# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grainGrowth', '0007_remove_mesh_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='IC',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('op_num', models.IntegerField(default=10, verbose_name=b'number of order paramaters')),
                ('grain_num', models.IntegerField(default=10, verbose_name=b'number of grains')),
                ('var_name_base', models.CharField(default=b'gr', max_length=10, verbose_name=b'base name of grains')),
                ('T', models.FloatField(default=450, verbose_name=b'temperature')),
            ],
        ),
        migrations.CreateModel(
            name='Outputs',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('exodus', models.CharField(max_length=5, verbose_name=b'exodus file is exported?', choices=[(b'true', b'true'), (b'false', b'false')])),
                ('csv', models.CharField(max_length=5, verbose_name=b'csv file is exported?', choices=[(b'true', b'true'), (b'false', b'false')])),
            ],
        ),
        migrations.RemoveField(
            model_name='materials',
            name='T',
        ),
        migrations.RemoveField(
            model_name='materials',
            name='name',
        ),
        migrations.AddField(
            model_name='mesh',
            name='uniform_refine',
            field=models.IntegerField(default=2, verbose_name=b'initial uniform refinement'),
        ),
    ]
