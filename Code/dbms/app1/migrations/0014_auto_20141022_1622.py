# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0013_auto_20141021_1802'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mobile',
            name='pid',
            field=models.ForeignKey(to='app1.Good', unique=True),
        ),
    ]
