# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-08 16:39
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0007_alter_validators_add_error_messages'),
        ('elearning', '0002_htmlblock_quizblock_videoblock'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('dob', models.DateField()),
                ('role', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='elearning.Role')),
            ],
            options={
                'abstract': False,
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='role',
        ),
        migrations.AlterField(
            model_name='course',
            name='users',
            field=models.ManyToManyField(to='elearning.CustomUser'),
        ),
        migrations.AlterField(
            model_name='programme',
            name='users',
            field=models.ManyToManyField(to='elearning.CustomUser'),
        ),
        migrations.AlterField(
            model_name='progress',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='elearning.CustomUser'),
        ),
        migrations.AlterField(
            model_name='rating',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='elearning.CustomUser'),
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
