# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-07-01 10:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20190701_1829'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='activated',
            field=models.IntegerField(null=True),
        ),
    ]
