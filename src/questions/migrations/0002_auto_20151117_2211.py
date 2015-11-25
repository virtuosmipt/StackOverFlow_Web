# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='title',
            field=models.CharField(max_length=10000, default='NEW QUESTION '),
        ),
        migrations.AddField(
            model_name='question_answer',
            name='text_answer',
            field=models.CharField(max_length=10000, default='SOME STRING'),
        ),
    ]
