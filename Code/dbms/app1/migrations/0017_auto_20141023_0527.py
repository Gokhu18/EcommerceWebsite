# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0016_auto_20141023_0424'),
    ]

    operations = [
        migrations.AlterField(
            model_name='laptop',
            name='battery',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='laptop',
            name='display_size',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='laptop',
            name='os',
            field=models.CharField(max_length=20),
        ),
    ]
