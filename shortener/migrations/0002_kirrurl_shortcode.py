# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-03-13 07:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='kirrurl',
            name='shortcode',
            field=models.CharField(default='defaultValue', max_length=15),
            preserve_default=False,
        ),
    ]
