# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_auto_20141012_1611'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='pwd',
            field=models.CharField(default=b'ABCD', max_length=20),
            preserve_default=True,
        ),
    ]
