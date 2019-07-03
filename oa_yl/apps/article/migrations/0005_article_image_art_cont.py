# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-07-03 03:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0004_article_title_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='article_image',
            name='art_cont',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='article.Article', verbose_name='文章内容'),
        ),
    ]