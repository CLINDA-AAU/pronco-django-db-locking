# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-09 13:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locking', '0005_merge_20170504_1024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nonblockinglock',
            name='max_age',
            field=models.PositiveIntegerField(default=0, help_text='The age of a lock before it can be overwritten. 0 means indefinitely.', verbose_name='Maximum lock age'),
        ),
    ]
