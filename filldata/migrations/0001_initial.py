# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('state', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('apartment', models.CharField(max_length=200)),
                ('block', models.CharField(max_length=200)),
                ('flat_no', models.CharField(max_length=200)),
                ('bhk', models.CharField(max_length=200)),
                ('rent', models.CharField(max_length=200)),
                ('date_added', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
