# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-02 00:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0004_auto_20160402_0042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='does_not_tolerate',
            field=models.CharField(blank=True, default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='tolerates',
            field=models.CharField(blank=True, default='', max_length=500),
        ),
    ]