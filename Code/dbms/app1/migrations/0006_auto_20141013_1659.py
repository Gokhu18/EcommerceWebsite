# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_customer_pwd'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='username',
            field=models.CharField(default=b'abcd', unique=True, max_length=30),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='customer',
            name='custid',
            field=models.PositiveIntegerField(default=0, max_length=30, unique=True, serialize=False, primary_key=True),
        ),
    ]
