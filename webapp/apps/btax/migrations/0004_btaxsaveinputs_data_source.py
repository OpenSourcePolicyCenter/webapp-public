# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-03-06 20:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('btax', '0003_auto_20180205_2151'),
    ]

    operations = [
        migrations.AddField(
            model_name='btaxsaveinputs',
            name='data_source',
            field=models.CharField(blank=True, default=b'PUF', max_length=20, null=True),
        ),
    ]
