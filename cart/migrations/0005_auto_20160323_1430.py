# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-23 14:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0004_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='selling_ends_on',
            field=models.DateField(blank=True),
        ),
    ]