# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-01-19 15:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0016_auto_20160608_1535'),
        ('blog', '0005_auto_20171202_0941'),
    ]

    operations = [
        migrations.CreateModel(
            name='RecentPosts',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='blog_recentposts', serialize=False, to='cms.CMSPlugin')),
                ('recent_posts_number', models.SmallIntegerField(default=5)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]