# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-15 12:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0003_auto_20171112_1712'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='vn30',
            field=models.BooleanField(default=False),
        ),
    ]
