# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0019_remove_fashion_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fashion',
            name='prod_type',
            field=models.CharField(max_length=20),
        ),
    ]
