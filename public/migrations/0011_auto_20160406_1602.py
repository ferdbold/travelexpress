# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-06 20:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0010_trip_quit_counts'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trip',
            name='quit_counts',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='quit_counts',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]