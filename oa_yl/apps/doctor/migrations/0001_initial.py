# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-07-01 01:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('hospital', '0001_initial'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doc_adv',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField(default=5, verbose_name='评分')),
                ('doc_con', models.CharField(default='默认好评', max_length=200, verbose_name='评论内容')),
                ('doc_time', models.DateTimeField(auto_now_add=True, verbose_name='评论时间')),
            ],
            options={
                'verbose_name': '我的问诊表',
                'verbose_name_plural': '我的问诊表',
                'db_table': 'doc_adv',
            },
        ),
        migrations.CreateModel(
            name='Doc_comm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nick_name', models.CharField(default='匿名用户', max_length=20, verbose_name='用户名')),
                ('score', models.IntegerField(default=5, verbose_name='评分')),
                ('comm_con', models.CharField(default='默认好评', max_length=200, verbose_name='评论内容')),
                ('comm_time', models.DateTimeField(auto_now_add=True, verbose_name='评论时间')),
            ],
            options={
                'verbose_name': '医生评价表',
                'verbose_name_plural': '医生评价表',
                'db_table': 'doc_comm',
            },
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doc_name', models.CharField(max_length=50, verbose_name='医生姓名')),
                ('doc_title', models.CharField(max_length=50, verbose_name='职称')),
                ('doc_img', models.CharField(max_length=255, verbose_name='照片')),
                ('doc_exp', models.CharField(max_length=15, verbose_name='从业时间')),
                ('doc_goods', models.CharField(max_length=255, verbose_name='擅长方向')),
                ('doc_resume', models.TextField(verbose_name='医生履历')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital.Department', verbose_name='医生科室')),
                ('hospital', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital.Hospital', verbose_name='所属医院')),
            ],
            options={
                'verbose_name': '医生表',
                'verbose_name_plural': '医生表',
                'db_table': 'doctors',
            },
        ),
        migrations.CreateModel(
            name='DoctorQuality',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('d_level', models.IntegerField(default=5, verbose_name='评分')),
                ('m_answer', models.CharField(max_length=20, verbose_name='月回答次数')),
                ('m_recipel', models.IntegerField(verbose_name='月处方数量')),
                ('avg_response', models.IntegerField(verbose_name='平均回复时间')),
                ('is_recommend', models.BooleanField(default=False, verbose_name='是否力荐')),
                ('text_price', models.CharField(max_length=20, verbose_name='图文问诊价格')),
                ('tel_price', models.CharField(max_length=50, verbose_name='电话问诊价格')),
                ('d_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctor.Doctor', verbose_name='医生')),
            ],
            options={
                'verbose_name': '医生属性表',
                'verbose_name_plural': '医生属性表',
                'db_table': 'doctor_quality',
            },
        ),
        migrations.CreateModel(
            name='Focus_doc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('arc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctor.Doctor')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.User')),
            ],
            options={
                'db_table': 'focus_doc',
            },
        ),
        migrations.AddField(
            model_name='doc_comm',
            name='doc_comm',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctor.Doctor', verbose_name='医生名称'),
        ),
        migrations.AddField(
            model_name='doc_adv',
            name='doc_adv',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctor.Doctor', verbose_name='医生名称'),
        ),
        migrations.AddField(
            model_name='doc_adv',
            name='u_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.User', verbose_name='用户名'),
        ),
    ]
