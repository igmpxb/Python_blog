# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-28 06:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_click_rate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='creater_time',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='post',
            name='modified_time',
            field=models.DateTimeField(),
        ),
    ]