# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-14 18:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('neighborhoods', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='neighborhoodboundaries',
            name='id',
        ),
        migrations.AlterField(
            model_name='neighborhoodboundaries',
            name='objectid',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]