# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-06-08 23:51
from __future__ import unicode_literals

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_userprofile_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='email',
            field=models.EmailField(blank=True, max_length=32, null=True, verbose_name=django.contrib.auth.models.User),
        ),
    ]
