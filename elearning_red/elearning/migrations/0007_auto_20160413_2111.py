# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-13 21:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elearning', '0006_auto_20160413_2059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='block',
            name='index',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='block',
            name='name',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]
