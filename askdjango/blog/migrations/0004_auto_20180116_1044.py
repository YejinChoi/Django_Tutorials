# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-16 10:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20180116_1029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='tags',
            field=models.CharField(max_length=100),
        ),
    ]
