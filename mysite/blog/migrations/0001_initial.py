# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-10-05 11:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Browse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('computer', models.CharField(blank=True, max_length=10, null=True)),
                ('mobilephone', models.CharField(blank=True, max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tvname', models.FloatField(choices=[('Design', 'Design'), ('Other', 'Other'), ('Manufacture', 'Manufacture')], default='Design', max_length=20)),
                ('name', models.CharField(blank=True, max_length=20, null=True)),
                ('lineroad', models.CharField(blank=True, max_length=6, null=True)),
                ('url', models.CharField(blank=True, max_length=120, null=True)),
                ('date', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
    ]
