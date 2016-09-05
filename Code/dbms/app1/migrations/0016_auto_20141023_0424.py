# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0015_auto_20141022_1628'),
    ]

    operations = [
        migrations.AlterField(
            model_name='laptop',
            name='processor',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='mobile',
            name='processor',
            field=models.CharField(max_length=40),
        ),
    ]
