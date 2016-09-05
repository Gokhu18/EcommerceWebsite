# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0017_auto_20141023_0527'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='pid',
            field=models.ForeignKey(to='app1.Good'),
        ),
    ]
