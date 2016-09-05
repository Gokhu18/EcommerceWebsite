# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0020_auto_20141023_0620'),
    ]

    operations = [
        migrations.AlterField(
            model_name='media',
            name='media_type',
            field=models.CharField(max_length=20),
        ),
    ]
