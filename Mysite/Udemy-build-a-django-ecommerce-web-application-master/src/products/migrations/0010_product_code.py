# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-05-21 15:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_product_timestamp'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='code',
            field=models.TextField(blank=True),
        ),
    ]