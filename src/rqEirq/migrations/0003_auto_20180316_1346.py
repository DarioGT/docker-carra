# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rqEirq', '0002_auto_20180315_1416'),
    ]

    operations = [
        migrations.AddField(
            model_name='fichier',
            name='label',
            field=models.CharField(null=True, blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='responsable',
            name='label',
            field=models.CharField(null=True, blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='source',
            name='label',
            field=models.CharField(null=True, blank=True, max_length=200),
        ),
    ]
