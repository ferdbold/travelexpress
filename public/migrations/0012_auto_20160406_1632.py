# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-06 20:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0011_auto_20160406_1602'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='quit_counts',
            new_name='quit_count',
        ),
    ]
