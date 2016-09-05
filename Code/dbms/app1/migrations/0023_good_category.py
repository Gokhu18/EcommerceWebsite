# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0022_remove_product_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='good',
            name='category',
            field=models.CharField(max_length=50, null=True),
            preserve_default=True,
        ),
    ]
