# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_ruben'),
    ]

    operations = [
        migrations.RenameField(
            model_name='javi',
            old_name='skillFirst',
            new_name='skill',
        ),
        migrations.RenameField(
            model_name='ruben',
            old_name='skillFirst',
            new_name='skill',
        ),
        migrations.RemoveField(
            model_name='javi',
            name='age',
        ),
        migrations.RemoveField(
            model_name='javi',
            name='name',
        ),
        migrations.RemoveField(
            model_name='javi',
            name='photo',
        ),
        migrations.RemoveField(
            model_name='javi',
            name='sex',
        ),
        migrations.RemoveField(
            model_name='javi',
            name='skillForth',
        ),
        migrations.RemoveField(
            model_name='javi',
            name='skillSecond',
        ),
        migrations.RemoveField(
            model_name='javi',
            name='skillThird',
        ),
        migrations.RemoveField(
            model_name='ruben',
            name='age',
        ),
        migrations.RemoveField(
            model_name='ruben',
            name='name',
        ),
        migrations.RemoveField(
            model_name='ruben',
            name='photo',
        ),
        migrations.RemoveField(
            model_name='ruben',
            name='sex',
        ),
        migrations.RemoveField(
            model_name='ruben',
            name='skillForth',
        ),
        migrations.RemoveField(
            model_name='ruben',
            name='skillSecond',
        ),
        migrations.RemoveField(
            model_name='ruben',
            name='skillThird',
        ),
    ]
