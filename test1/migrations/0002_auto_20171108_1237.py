# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-11-08 12:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adminmanager',
            name='age',
            field=models.IntegerField(default=18, verbose_name='\u5e74\u7eaa'),
        ),
        migrations.AlterField(
            model_name='adminmanager',
            name='image',
            field=models.ImageField(upload_to='uploads/images'),
        ),
    ]
