# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0007_remove_question_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='rate',
        ),
        migrations.AddField(
            model_name='question',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 16, 15, 40, 7, 943332, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
