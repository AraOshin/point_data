# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-14 18:30
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NeighborhoodBoundaries',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('objectid', models.IntegerField()),
                ('name', models.CharField(max_length=50)),
                ('commplan', models.CharField(max_length=50)),
                ('shared', models.CharField(max_length=50)),
                ('coalit', models.CharField(max_length=50)),
                ('horz_vert', models.CharField(max_length=50)),
                ('shape_length', models.FloatField()),
                ('maplabel', models.CharField(max_length=50)),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
            ],
        ),
    ]
