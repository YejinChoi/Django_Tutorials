# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-18 10:59
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_auto_20180117_0622'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog_post_set', to=settings.AUTH_USER_MODEL),
        ),
    ]
