# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-06-14 08:12
from __future__ import unicode_literals

import django.contrib.auth.models
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_auto_20190613_1630'),
    ]

    operations = [
        migrations.CreateModel(
            name='PremiumProject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('description', models.CharField(max_length=255)),
                ('status', models.CharField(choices=[('Work', 'Work'), ('Education', 'Education'), ('Personal', 'Personal')], default='Work', max_length=40)),
                ('assign', models.CharField(max_length=40, verbose_name=django.contrib.auth.models.User)),
                ('published_date', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
            ],
        ),
    ]