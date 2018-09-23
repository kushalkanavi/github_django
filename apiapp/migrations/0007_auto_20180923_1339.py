# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-09-23 13:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiapp', '0006_auto_20180923_1338'),
    ]

    operations = [
        migrations.AddField(
            model_name='githubapi',
            name='followers',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='githubapi',
            name='following',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='githubapi',
            name='public_gists',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='githubapi',
            name='public_repos',
            field=models.IntegerField(null=True),
        ),
    ]
