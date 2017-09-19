# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-11 16:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('pub_time', models.DateTimeField()),
                ('text', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Sheet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('album', models.CharField(max_length=20)),
                ('music', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True)),
                ('email', models.EmailField(default='', max_length=254)),
                ('gender', models.BooleanField(default=True)),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='artical',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='piano.Sheet'),
        ),
    ]