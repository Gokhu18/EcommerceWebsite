# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0018_auto_20141023_0607'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fashion',
            name='category',
        ),
    ]
