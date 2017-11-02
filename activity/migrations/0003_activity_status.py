# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-16 20:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0002_remove_activity_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='status',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='activity.ActivityStatus'),
            preserve_default=False,
        ),
    ]
