# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-11-09 08:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0004_auto_20181108_1602'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wheel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.CharField(max_length=256)),
            ],
        ),
    ]