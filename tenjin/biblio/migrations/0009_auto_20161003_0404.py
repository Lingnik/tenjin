# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-03 04:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biblio', '0008_auto_20161003_0341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publication',
            name='editors',
            field=models.ManyToManyField(blank=True, null=True, to='biblio.Author'),
        ),
    ]