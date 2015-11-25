# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0004_auto_20151125_1323'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='date',
        ),
        migrations.RemoveField(
            model_name='question',
            name='rate',
        ),
    ]
