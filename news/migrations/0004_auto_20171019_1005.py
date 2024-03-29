# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-19 14:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_auto_20171017_1511'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='activity',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='activity.Activity'),
        ),
        migrations.AlterField(
            model_name='news',
            name='status',
            field=models.IntegerField(choices=[(1, 'Online'), (2, 'Draft')], max_length=2),
        ),
    ]
