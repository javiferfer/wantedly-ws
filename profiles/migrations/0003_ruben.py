# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_auto_20171212_1420'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ruben',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=25)),
                ('age', models.IntegerField()),
                ('sex', models.CharField(max_length=10)),
                ('photo', models.CharField(max_length=1000)),
                ('skillFirst', models.CharField(max_length=250)),
                ('skillSecond', models.CharField(max_length=250)),
                ('skillThird', models.CharField(max_length=250)),
                ('skillForth', models.CharField(max_length=250)),
            ],
        ),
    ]
