# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-09-23 13:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiapp', '0002_auto_20180923_1335'),
    ]

    operations = [
        migrations.AddField(
            model_name='githubapi',
            name='avatar_url',
            field=models.URLField(max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='githubapi',
            name='gravatar_id',
            field=models.IntegerField(null=True),
        ),
    ]
