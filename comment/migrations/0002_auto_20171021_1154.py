# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-21 15:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='authorId',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='newsId',
            new_name='news',
        ),
    ]