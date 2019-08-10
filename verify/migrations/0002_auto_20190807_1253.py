# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-08-07 12:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('verify', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messages',
            name='M_FromUserID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='发送者ID', to='verify.User'),
        ),
        migrations.AlterField(
            model_name='messages',
            name='M_ToUserID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='接收者ID', to='verify.User'),
        ),
    ]