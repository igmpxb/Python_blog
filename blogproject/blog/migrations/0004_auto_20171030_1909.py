# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-30 11:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20171028_1427'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='img_url',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AddField(
            model_name='post',
            name='top_weight',
            field=models.IntegerField(default=0),
        ),
    ]
