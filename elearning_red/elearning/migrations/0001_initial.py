# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-04 16:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Block',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('index', models.PositiveSmallIntegerField()),
                ('assessment', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('desc', models.TextField()),
                ('beginDate', models.DateField()),
                ('duration', models.PositiveSmallIntegerField()),
                ('author', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Permission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Programme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('desc', models.TextField()),
                ('avgRating', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='Progress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serialAnswers', models.TextField()),
                ('block', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='elearning.Block')),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.PositiveSmallIntegerField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='elearning.Course')),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('permissions', models.ManyToManyField(to='elearning.Permission')),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('desc', models.TextField()),
                ('beginDate', models.DateField()),
                ('index', models.PositiveSmallIntegerField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='elearning.Course')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=25)),
                ('password', models.CharField(max_length=25)),
                ('email', models.EmailField(max_length=254)),
                ('firstName', models.CharField(max_length=25)),
                ('lastName', models.CharField(max_length=25)),
                ('dob', models.DateField()),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='elearning.Role')),
            ],
        ),
        migrations.AddField(
            model_name='rating',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='elearning.User'),
        ),
        migrations.AddField(
            model_name='progress',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='elearning.User'),
        ),
        migrations.AddField(
            model_name='programme',
            name='tags',
            field=models.ManyToManyField(to='elearning.Tag'),
        ),
        migrations.AddField(
            model_name='programme',
            name='users',
            field=models.ManyToManyField(to='elearning.User'),
        ),
        migrations.AddField(
            model_name='course',
            name='programmes',
            field=models.ManyToManyField(to='elearning.Programme'),
        ),
        migrations.AddField(
            model_name='course',
            name='tags',
            field=models.ManyToManyField(to='elearning.Tag'),
        ),
        migrations.AddField(
            model_name='course',
            name='users',
            field=models.ManyToManyField(to='elearning.User'),
        ),
        migrations.AddField(
            model_name='block',
            name='sections',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='elearning.Section'),
        ),
    ]
