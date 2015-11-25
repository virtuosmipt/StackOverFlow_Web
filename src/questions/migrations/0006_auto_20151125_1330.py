# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0005_auto_20151125_1329'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2015, 11, 25, 13, 30, 27, 542673, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='rate',
            field=models.IntegerField(default=0),
        ),
    ]
