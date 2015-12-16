# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0008_auto_20151216_1540'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='date',
        ),
    ]
