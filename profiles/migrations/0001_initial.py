# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Javi',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=25)),
                ('age', models.CharField(max_length=250)),
                ('sex', models.CharField(max_length=10)),
                ('photo', models.CharField(max_length=1000)),
                ('skillFirst', models.CharField(max_length=250)),
                ('skillSecond', models.CharField(max_length=250)),
                ('skillThird', models.CharField(max_length=250)),
                ('skillFourth', models.CharField(max_length=250)),
            ],
        ),
    ]
