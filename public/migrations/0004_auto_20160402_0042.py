# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-02 00:42
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0003_auto_20160401_0431'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='does_not_tolerate',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='tolerates',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='trip',
            name='destination',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='trip',
            name='origin',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='phone',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL),
        ),
    ]