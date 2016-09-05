# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_customeritems'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='custid',
            field=models.CharField(default=0, max_length=30, serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='email',
            field=models.EmailField(unique=True, max_length=75),
        ),
    ]
