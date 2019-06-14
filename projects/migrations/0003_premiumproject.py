# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-06-13 16:22
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projects', '0002_project_published_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='PremiumProject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('description', models.CharField(max_length=255)),
                ('status', models.CharField(choices=[('Work', 'Work'), ('Education', 'Education'), ('Personal', 'Personal')], default='Work', max_length=40)),
                ('assign', models.CommaSeparatedIntegerField(blank=True, max_length=10)),
                ('published_date', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
