# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0007_auto_20141013_1715'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='username',
        ),
    ]
