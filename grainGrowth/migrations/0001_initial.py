# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Executioner',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dt', models.FloatField(default=5, verbose_name=b'time step')),
                ('end_time', models.FloatField(default=4000, verbose_name=b'end time')),
            ],
        ),
        migrations.CreateModel(
            name='Materials',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('GBmob0', models.FloatField(default=2.5e-06, verbose_name=b'mobility prefactor')),
                ('GBenergy', models.FloatField(default=0.708, verbose_name=b'grain boundary energy')),
                ('Q', models.FloatField(default=0.23, verbose_name=b'activation energy')),
                ('T', models.FloatField(default=450, verbose_name=b'temperature')),
                ('wGB', models.FloatField(default=14, verbose_name=b'width of grain boundary')),
            ],
        ),
        migrations.CreateModel(
            name='Mesh',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dim', models.IntegerField(default=2, verbose_name=b'model dimension')),
                ('nx', models.IntegerField(default=10, verbose_name=b'number of elements in x-direction')),
                ('ny', models.IntegerField(default=10, verbose_name=b'number of elements in y-direction')),
                ('nz', models.IntegerField(default=0, verbose_name=b'number of elements in z-direction')),
                ('xmin', models.FloatField(default=0, verbose_name=b'minium x-coordinate of the mesh')),
                ('ymin', models.FloatField(default=0, verbose_name=b'minium y-coordinate of the mesh')),
                ('zmin', models.FloatField(default=0, verbose_name=b'minium z-coordinate of the mesh')),
                ('xmax', models.FloatField(default=1000, verbose_name=b'maximum x-coordinate of the mesh')),
                ('ymax', models.FloatField(default=1000, verbose_name=b'maximum y-coordinate of the mesh')),
                ('zmax', models.FloatField(default=0, verbose_name=b'maximum z-coordinate of the mesh')),
            ],
        ),
    ]
