# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-07 02:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0012_auto_20160406_1632'),
    ]

    operations = [
        migrations.AddField(
            model_name='trip',
            name='is_completed',
            field=models.BooleanField(default=False),
        ),
    ]
