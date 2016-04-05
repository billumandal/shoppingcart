# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-23 14:17
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cart', '0002_auto_20160326_1308'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='buyer',
        ),
        migrations.AddField(
            model_name='transaction',
            name='buyer',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='transaction_buyer', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='product',
        ),
        migrations.AddField(
            model_name='transaction',
            name='product',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='cart.Product'),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='seller',
        ),
        migrations.AddField(
            model_name='transaction',
            name='seller',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='transaction_seller', to='cart.UserProfile'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='transaction',
            name='time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]