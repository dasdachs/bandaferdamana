# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-12-10 14:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0004_postindex'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='exposed',
            field=models.BooleanField(default=False),
        ),
    ]
