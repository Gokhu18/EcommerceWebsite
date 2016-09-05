# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_auto_20141003_2020'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerItems',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('qty', models.PositiveIntegerField(max_length=10)),
                ('custid', models.ForeignKey(to='app1.Customer')),
                ('pid', models.ForeignKey(to='app1.Product')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
