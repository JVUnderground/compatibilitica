# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answer',
            old_name='value',
            new_name='economic',
        ),
        migrations.AddField(
            model_name='answer',
            name='social',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]
