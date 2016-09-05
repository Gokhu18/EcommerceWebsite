# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('author', models.CharField(max_length=30)),
                ('book_type', models.CharField(max_length=30)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('name', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=75)),
                ('phoneno', models.PositiveIntegerField(max_length=10)),
                ('custid', models.CharField(max_length=30, serialize=False, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Fashion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('gender', models.CharField(max_length=10)),
                ('color', models.CharField(max_length=10)),
                ('category', models.CharField(max_length=10)),
                ('material', models.CharField(max_length=10)),
                ('size', models.CharField(max_length=10)),
                ('prod_type', models.CharField(max_length=10)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('brand', models.CharField(max_length=10)),
                ('product_name', models.CharField(max_length=30)),
                ('pid', models.PositiveIntegerField(default=0, serialize=False, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Laptop',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('battery', models.CharField(max_length=10)),
                ('os', models.CharField(max_length=10)),
                ('display_size', models.CharField(max_length=10)),
                ('processor', models.CharField(max_length=10)),
                ('ram', models.CharField(max_length=10)),
                ('storage', models.CharField(max_length=10)),
                ('pid', models.ForeignKey(to='app1.Goods')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('media_type', models.CharField(max_length=10)),
                ('pid', models.ForeignKey(to='app1.Goods')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Mobiles',
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
                ('pid', models.ForeignKey(to='app1.Goods')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('category', models.CharField(max_length=50)),
                ('price', models.PositiveIntegerField(max_length=60)),
                ('qty_left', models.PositiveIntegerField(max_length=30)),
                ('pid', models.CharField(max_length=20, serialize=False, primary_key=True)),
                ('discount', models.PositiveIntegerField()),
                ('accessories', models.CharField(max_length=60)),
                ('goodsid', models.ForeignKey(to='app1.Goods')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('sid', models.CharField(max_length=20, serialize=False, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=20)),
                ('delivery_time', models.PositiveIntegerField(max_length=10)),
                ('rating', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TV',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('display_size', models.CharField(max_length=10)),
                ('display_type', models.CharField(max_length=10)),
                ('features', models.CharField(max_length=50)),
                ('pid', models.ForeignKey(to='app1.Goods')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='product',
            name='sid',
            field=models.ForeignKey(to='app1.Seller'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='fashion',
            name='pid',
            field=models.ForeignKey(to='app1.Goods'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='books',
            name='pid',
            field=models.ForeignKey(to='app1.Product'),
            preserve_default=True,
        ),
    ]
