# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-07-03 09:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order_detail',
            name='o_addr',
            field=models.CharField(max_length=200, null=True, verbose_name='收货地址'),
        ),
        migrations.AlterField(
            model_name='order_detail',
            name='o_consignee',
            field=models.CharField(max_length=20, null=True, verbose_name='收货人'),
        ),
        migrations.AlterField(
            model_name='order_detail',
            name='o_phone',
            field=models.CharField(max_length=15, null=True, verbose_name='收货人手机号'),
        ),
    ]
