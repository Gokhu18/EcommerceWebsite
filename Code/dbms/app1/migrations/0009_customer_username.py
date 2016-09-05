# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0008_remove_customer_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='username',
            field=models.CharField(default=datetime.date(2014, 10, 14), max_length=30),
            preserve_default=False,
        ),
    ]
