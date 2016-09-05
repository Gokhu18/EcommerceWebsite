# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0010_auto_20141014_1814'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mobile',
            name='category',
        ),
    ]
