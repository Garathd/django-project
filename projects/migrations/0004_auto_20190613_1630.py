# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-06-13 16:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_premiumproject'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='premiumproject',
            name='user',
        ),
        migrations.DeleteModel(
            name='PremiumProject',
        ),
    ]
