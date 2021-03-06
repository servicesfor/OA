# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-07-03 08:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0005_auto_20190701_1831'),
        ('medicine', '0002_auto_20190702_1921'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('o_price', models.FloatField(default=0, verbose_name='订单总价')),
                ('o_status', models.IntegerField(default=0, verbose_name='订单状态')),
                ('o_id', models.CharField(max_length=30, unique=True, verbose_name='订单号')),
                ('o_time', models.DateTimeField(auto_now=True, null=True, verbose_name='下单时间')),
                ('o_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.User', verbose_name='用户')),
            ],
            options={
                'verbose_name': '订单表',
                'verbose_name_plural': '订单表',
                'db_table': 'orders',
            },
        ),
        migrations.CreateModel(
            name='Order_Detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('o_consignee', models.CharField(max_length=20, verbose_name='收货人')),
                ('o_addr', models.CharField(max_length=200, verbose_name='收货地址')),
                ('o_phone', models.CharField(max_length=15, verbose_name='收货人手机号')),
                ('o_goods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medicine.Medicine', verbose_name='订单药品')),
                ('o_order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.Order', to_field='o_id', verbose_name='订单号')),
            ],
            options={
                'verbose_name': '订单详情表',
                'verbose_name_plural': '订单详情表',
                'db_table': 'order_detail',
            },
        ),
    ]
