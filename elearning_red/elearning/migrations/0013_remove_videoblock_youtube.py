# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-16 21:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('elearning', '0012_videoblock_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='videoblock',
            name='youtube',
        ),
    ]
