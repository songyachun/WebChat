# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-07-20 12:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User_info',
            fields=[
                ('uid', models.AutoField(primary_key=True, serialize=False)),
                ('nickname', models.CharField(max_length=128, verbose_name='昵称')),
                ('sex', models.IntegerField(verbose_name='性别')),
                ('age', models.IntegerField(verbose_name='年龄')),
                ('profile_head', models.CharField(max_length=255, null=True, verbose_name='头像')),
                ('profile', models.CharField(max_length=255, null=True, verbose_name='个性签名')),
            ],
        ),
        migrations.CreateModel(
            name='User_user',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=128, unique=True, verbose_name='用户名')),
                ('password', models.CharField(max_length=128, verbose_name='密码')),
                ('email', models.EmailField(max_length=254, verbose_name='邮箱')),
                ('mobile_number', models.CharField(max_length=128, verbose_name='手机号码')),
                ('login_time', models.DateTimeField(auto_now=True, verbose_name='登录时间')),
                ('logout_time', models.DateTimeField(auto_now=True, verbose_name='退出时间')),
                ('creat_time', models.DateTimeField(auto_now_add=True, verbose_name='注册时间')),
                ('ip_address', models.CharField(max_length=15, verbose_name='IP地址')),
                ('is_active', models.IntegerField(verbose_name='是否有效')),
            ],
        ),
        migrations.AddField(
            model_name='user_info',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='database.User_user'),
        ),
    ]