# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0006_auto_20151125_1330'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='date',
        ),
    ]
