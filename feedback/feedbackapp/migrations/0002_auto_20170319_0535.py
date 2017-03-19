# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-19 05:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedbackapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='division',
            field=models.CharField(default='NA', max_length=600),
        ),
        migrations.AddField(
            model_name='teacher',
            name='isPractical',
            field=models.BooleanField(default=False),
        ),
    ]
