# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0002_auto_20151117_2211'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='text_question',
            field=models.CharField(default='SOME STRING', max_length=10000),
        ),
    ]
