# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-02 14:11
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    replaces = [('elearning', '0001_initial'), ('elearning', '0002_htmlblock_quizblock_videoblock'), ('elearning', '0003_auto_20160408_1723'), ('elearning', '0004_auto_20160422_1245'), ('elearning', '0005_auto_20160501_2145')]

    initial = True

    dependencies = [
        ('auth', '0007_alter_validators_add_error_messages'),
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
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='elearning.CustomUser')),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('permissions', models.ManyToManyField(to=b'elearning.Permission')),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('desc', models.TextField(blank=True, null=True)),
                ('beginDate', models.DateField(blank=True, null=True)),
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
            model_name='progress',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='elearning.CustomUser'),
        ),
        migrations.AddField(
            model_name='programme',
            name='tags',
            field=models.ManyToManyField(blank=True, to=b'elearning.Tag'),
        ),
        migrations.AddField(
            model_name='programme',
            name='users',
            field=models.ManyToManyField(blank=True, to=b'elearning.CustomUser'),
        ),
        migrations.AddField(
            model_name='course',
            name='programmes',
            field=models.ManyToManyField(blank=True, to=b'elearning.Programme'),
        ),
        migrations.AddField(
            model_name='course',
            name='tags',
            field=models.ManyToManyField(blank=True, to=b'elearning.Tag'),
        ),
        migrations.AddField(
            model_name='course',
            name='users',
            field=models.ManyToManyField(blank=True, to=b'elearning.CustomUser'),
        ),
        migrations.AddField(
            model_name='block',
            name='sections',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='elearning.Section'),
        ),
        migrations.CreateModel(
            name='HTMLBlock',
            fields=[
                ('block_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='elearning.Block')),
                ('content', models.TextField()),
            ],
            bases=('elearning.block',),
        ),
        migrations.CreateModel(
            name='QuizBlock',
            fields=[
                ('block_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='elearning.Block')),
                ('serialQuestions', models.TextField()),
            ],
            bases=('elearning.block',),
        ),
        migrations.CreateModel(
            name='VideoBlock',
            fields=[
                ('block_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='elearning.Block')),
                ('url', models.URLField(default='https://www.youtube.com/watch?v=dQw4w9WgXcQ', max_length=250)),
            ],
            bases=('elearning.block',),
        ),
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
        migrations.DeleteModel(
            name='User',
        ),
        migrations.CreateModel(
            name='ImageBlock',
            fields=[
                ('block_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='elearning.Block')),
                ('subtitle', models.CharField(blank=True, max_length=40, null=True)),
                ('image', models.ImageField(upload_to='')),
            ],
            bases=('elearning.block',),
        ),
        migrations.AddField(
            model_name='course',
            name='avgRating',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='block',
            name='assessment',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='course',
            name='author',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='beginDate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='desc',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='duration',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='programme',
            name='avgRating',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='role',
            name='permissions',
            field=models.ManyToManyField(blank=True, to=b'elearning.Permission'),
        ),
    ]
