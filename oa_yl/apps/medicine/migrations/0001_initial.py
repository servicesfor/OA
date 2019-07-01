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
            name='Med_Details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('composition', models.CharField(max_length=500, verbose_name='药品成分')),
                ('shape', models.CharField(max_length=500, verbose_name='药品形状')),
                ('indications', models.TextField(verbose_name='适应症')),
                ('pdc_date', models.CharField(max_length=50, verbose_name='生产日期')),
                ('validity_period', models.CharField(max_length=20, verbose_name='有效期')),
                ('manufacturer', models.TextField(verbose_name='制造商')),
                ('med_interact', models.TextField(verbose_name='药品相互作用')),
                ('attentions', models.TextField(verbose_name='注意事项')),
                ('taboo', models.TextField(verbose_name='禁忌')),
                ('reaction', models.TextField(verbose_name='不良反应')),
                ('pharm_toxicity', models.TextField(verbose_name='药理毒理')),
                ('storage', models.CharField(max_length=255, verbose_name='贮藏')),
            ],
            options={
                'verbose_name': '药品详情表',
                'verbose_name_plural': '药品详情表',
                'db_table': 'med_details',
            },
        ),
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('med_name', models.CharField(max_length=200, unique=True, verbose_name='药品名')),
                ('med_img', models.CharField(max_length=255, verbose_name='药品图片')),
                ('price', models.CharField(max_length=50, verbose_name='药品价格')),
                ('med_stock', models.IntegerField(verbose_name='药品库存')),
                ('approval_number', models.CharField(max_length=50, verbose_name='批准文号')),
                ('packing_size', models.CharField(max_length=100, verbose_name='包装规格')),
                ('med_formulation', models.CharField(max_length=50, verbose_name='剂型')),
            ],
            options={
                'verbose_name': '药品表',
                'verbose_name_plural': '药品表',
                'db_table': 'medicine',
            },
        ),
        migrations.CreateModel(
            name='Mid_comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nick_name', models.CharField(default='匿名用户', max_length=20, verbose_name='用户名')),
                ('score', models.IntegerField(default=5, verbose_name='评分')),
                ('comm_con', models.CharField(default='默认好评', max_length=200, verbose_name='评论内容')),
                ('comm_time', models.DateTimeField(auto_now_add=True, verbose_name='评论时间')),
                ('med_comm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medicine.Medicine', to_field='med_name', verbose_name='药品名称')),
            ],
            options={
                'verbose_name': '药品评论表',
                'verbose_name_plural': '药品评论表',
                'db_table': 'mid_comm',
            },
        ),
        migrations.AddField(
            model_name='med_details',
            name='med_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medicine.Medicine', verbose_name='药品名称'),
        ),
    ]
