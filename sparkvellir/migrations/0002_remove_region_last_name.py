# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-04-22 14:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sparkvellir', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='region',
            name='last_name',
        ),
    ]
