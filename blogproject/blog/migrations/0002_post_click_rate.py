# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-28 05:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='click_rate',
            field=models.IntegerField(default=0),
        ),
    ]