# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-03 04:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biblio', '0010_auto_20161003_0410'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='abstract',
            field=models.TextField(blank=True, null=True),
        ),
    ]
