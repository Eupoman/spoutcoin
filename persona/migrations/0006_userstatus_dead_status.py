# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-15 03:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0005_auto_20171114_1136'),
    ]

    operations = [
        migrations.AddField(
            model_name='userstatus',
            name='dead_status',
            field=models.BooleanField(default=False),
        ),
    ]
