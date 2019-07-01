# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-07-01 01:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=15, verbose_name='城市')),
            ],
            options={
                'verbose_name': '城市表',
                'verbose_name_plural': '城市表',
                'db_table': 'cities',
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='科室名称')),
            ],
            options={
                'verbose_name': '科室表',
                'verbose_name_plural': '科室表',
                'db_table': 'departments',
            },
        ),
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hosp_name', models.CharField(max_length=100, verbose_name='医院名称')),
                ('hosp_addr', models.CharField(max_length=100, verbose_name='医院地址')),
                ('hosp_tel', models.CharField(max_length=30, verbose_name='医院电话')),
                ('medical_insurance', models.CharField(default='医保定点', max_length=20, verbose_name='医保')),
                ('hosp_level', models.CharField(max_length=20, verbose_name='医院级别')),
                ('hosp_img', models.CharField(max_length=255, verbose_name='医院图片')),
            ],
            options={
                'verbose_name': '医院表',
                'verbose_name_plural': '医院表',
                'db_table': 'hospitals',
            },
        ),
        migrations.CreateModel(
            name='Province',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pro_name', models.CharField(max_length=15, unique=True, verbose_name='省份')),
            ],
            options={
                'verbose_name': '省份表',
                'verbose_name_plural': '省份表',
                'db_table': 'provinces',
            },
        ),
        migrations.AddField(
            model_name='city',
            name='pro_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital.Province', to_field='pro_name', verbose_name='城市所在省份'),
        ),
    ]
