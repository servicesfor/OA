# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-07-01 10:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='nice_name',
            new_name='nick_name',
        ),
        migrations.AlterField(
            model_name='user',
            name='login_auth_str',
            field=models.CharField(max_length=200, null=True, verbose_name='口令'),
        ),
    ]
