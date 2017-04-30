# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-29 12:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Atmos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(blank=True, max_length=20)),
                ('sensor1_temp', models.CharField(max_length=100)),
                ('sensor2_temp', models.CharField(max_length=100)),
                ('sensor3_temp', models.CharField(max_length=100)),
                ('sensor4_temp', models.CharField(max_length=100)),
            ],
        ),
    ]
