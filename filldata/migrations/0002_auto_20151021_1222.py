# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filldata', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='state',
            new_name='name',
        ),
    ]
