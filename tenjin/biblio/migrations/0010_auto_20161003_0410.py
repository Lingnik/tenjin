# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-03 04:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biblio', '0009_auto_20161003_0404'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='abstract',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
        migrations.AddField(
            model_name='content',
            name='cited_by_scholar',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
