# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-02 14:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0006_artical_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artical',
            name='img_url',
            field=models.CharField(default=b'', max_length=100),
        ),
    ]
