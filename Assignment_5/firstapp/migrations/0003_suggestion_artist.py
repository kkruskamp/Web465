# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-13 01:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0002_artist'),
    ]

    operations = [
        migrations.AddField(
            model_name='suggestion',
            name='artist',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='firstapp.Artist'),
        ),
    ]
