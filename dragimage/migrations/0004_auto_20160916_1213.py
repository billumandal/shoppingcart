# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-09-16 06:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dragimage', '0003_auto_20160916_1208'),
    ]

    operations = [
        migrations.AddField(
            model_name='fourthtry',
            name='picture_name',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='fourthtry',
            name='picture_id',
            field=models.AutoField(max_length=20, primary_key=True, serialize=False),
        ),
    ]