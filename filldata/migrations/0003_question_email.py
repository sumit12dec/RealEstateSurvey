# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('filldata', '0002_auto_20151021_1222'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='email',
            field=models.EmailField(default=datetime.datetime(2015, 10, 21, 12, 51, 8, 820908, tzinfo=utc), max_length=200),
            preserve_default=False,
        ),
    ]
