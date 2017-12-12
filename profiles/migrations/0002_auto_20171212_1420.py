# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='javi',
            old_name='skillFourth',
            new_name='skillForth',
        ),
        migrations.AlterField(
            model_name='javi',
            name='age',
            field=models.IntegerField(),
        ),
    ]
