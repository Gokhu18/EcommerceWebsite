# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('author', models.CharField(max_length=30)),
                ('book_type', models.CharField(max_length=30)),
                ('pid', models.ForeignKey(to='app1.Product')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Mobile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('simslots', models.PositiveIntegerField(default=1, max_length=2)),
                ('battery', models.CharField(max_length=10)),
                ('category', models.CharField(max_length=10)),
                ('os', models.CharField(max_length=10)),
                ('display_size', models.CharField(max_length=10)),
                ('processor', models.CharField(max_length=10)),
                ('secondary_camera', models.CharField(max_length=10)),
                ('primary_camera', models.CharField(max_length=10)),
                ('storage', models.CharField(max_length=10)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RenameModel(
            old_name='Goods',
            new_name='Good',
        ),
        migrations.RemoveField(
            model_name='books',
            name='pid',
        ),
        migrations.DeleteModel(
            name='Books',
        ),
        migrations.RemoveField(
            model_name='mobiles',
            name='pid',
        ),
        migrations.DeleteModel(
            name='Mobiles',
        ),
        migrations.AddField(
            model_name='mobile',
            name='pid',
            field=models.ForeignKey(to='app1.Good'),
            preserve_default=True,
        ),
    ]
