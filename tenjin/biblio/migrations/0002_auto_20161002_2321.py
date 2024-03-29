# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-02 23:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('biblio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='given_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='content',
            name='publication',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='biblio.Publication'),
        ),
        migrations.AlterField(
            model_name='content',
            name='url',
            field=models.CharField(blank=True, max_length=2083, null=True),
        ),
    ]
