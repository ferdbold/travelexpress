# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-07 02:20
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0015_auto_20160406_2212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='blocked_until',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]
