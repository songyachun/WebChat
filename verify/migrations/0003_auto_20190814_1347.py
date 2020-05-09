# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-08-14 13:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('verify', '0002_auto_20190807_1253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='age',
            field=models.IntegerField(blank=True, null=True, verbose_name='年龄'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='birthday',
            field=models.CharField(default='', max_length=100, null=True, verbose_name='生日'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='city_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='省份ID', to='verify.City'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='nickname',
            field=models.CharField(max_length=128, null=True, verbose_name='昵称'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='profile',
            field=models.CharField(default='', max_length=255, null=True, verbose_name='个性签名'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='profile_head',
            field=models.ImageField(blank=True, default='', null=True, upload_to='avatar/', verbose_name='头像'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='province_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='省份ID', to='verify.Province'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='sex',
            field=models.IntegerField(blank=True, null=True, verbose_name='性别'),
        ),
    ]