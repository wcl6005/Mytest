# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-03-25 11:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0009_auto_20180323_0950'),
    ]

    operations = [
        migrations.AddField(
            model_name='reply',
            name='guestbookname',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AlterField(
            model_name='guestbook',
            name='username',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AlterField(
            model_name='reply',
            name='username',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
    ]
