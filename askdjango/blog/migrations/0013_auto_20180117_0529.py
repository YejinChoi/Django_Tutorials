# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-17 05:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_auto_20180117_0518'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='tags',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
