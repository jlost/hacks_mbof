# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-23 00:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mbof', '0003_auto_20160222_1556'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]
