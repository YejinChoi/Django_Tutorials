# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-19 05:28
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dojo', '0002_auto_20180119_0155'),
    ]

    operations = [
        migrations.CreateModel(
            name='GameUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('server_name', models.CharField(choices=[('A', 'A 서버'), ('B', 'B 서버'), ('C', 'C 서버')], max_length=10)),
                ('user_name', models.CharField(max_length=20, validators=[django.core.validators.MinLengthValidator(3)])),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='gameuser',
            unique_together=set([('server_name', 'user_name')]),
        ),
    ]
