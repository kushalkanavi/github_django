# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-09-23 13:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiapp', '0003_auto_20180923_1335'),
    ]

    operations = [
        migrations.AddField(
            model_name='githubapi',
            name='events_url',
            field=models.URLField(max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='githubapi',
            name='followers_url',
            field=models.URLField(max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='githubapi',
            name='following_url',
            field=models.URLField(max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='githubapi',
            name='gists_url',
            field=models.URLField(max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='githubapi',
            name='html_url',
            field=models.URLField(max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='githubapi',
            name='organizations_url',
            field=models.URLField(max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='githubapi',
            name='received_events_url',
            field=models.URLField(max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='githubapi',
            name='repos_url',
            field=models.URLField(max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='githubapi',
            name='starred_url',
            field=models.URLField(max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='githubapi',
            name='subscriptions_url',
            field=models.URLField(max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='githubapi',
            name='url',
            field=models.URLField(max_length=512, null=True),
        ),
    ]
