# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-07-02 11:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_arti_title_article_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='auth_img',
            field=models.CharField(default=1, max_length=200, verbose_name='作者头像'),
            preserve_default=False,
        ),
    ]