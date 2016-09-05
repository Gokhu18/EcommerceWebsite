# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0014_auto_20141022_1622'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mobile',
            name='processor',
            field=models.CharField(max_length=20),
        ),
    ]
