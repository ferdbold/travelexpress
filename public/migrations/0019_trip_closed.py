# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-08 03:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0018_auto_20160407_1942'),
    ]

    operations = [
        migrations.AddField(
            model_name='trip',
            name='closed',
            field=models.BooleanField(default=False),
        ),
    ]