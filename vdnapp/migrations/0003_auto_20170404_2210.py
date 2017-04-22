# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-04 22:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vdnapp', '0002_auto_20170404_2132'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dataset',
            name='dataset',
        ),
        migrations.RemoveField(
            model_name='dataset',
            name='frames',
        ),
        migrations.RemoveField(
            model_name='dataset',
            name='height',
        ),
        migrations.RemoveField(
            model_name='dataset',
            name='length_in_seconds',
        ),
        migrations.RemoveField(
            model_name='dataset',
            name='metadata',
        ),
        migrations.RemoveField(
            model_name='dataset',
            name='uploaded',
        ),
        migrations.RemoveField(
            model_name='dataset',
            name='width',
        ),
        migrations.AddField(
            model_name='dataset',
            name='download_url',
            field=models.TextField(default=''),
        ),
    ]