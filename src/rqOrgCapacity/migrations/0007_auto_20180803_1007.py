# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rqOrgCapacity', '0006_auto_20180803_0957'),
    ]

    operations = [
        migrations.AddField(
            model_name='skill',
            name='capacityAssigned',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='skill',
            name='capacityAvailable',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='skill',
            name='capacityGap',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='skill',
            name='capacityNeed',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
