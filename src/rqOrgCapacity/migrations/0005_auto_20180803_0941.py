# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rqOrgCapacity', '0004_auto_20180802_1654'),
    ]

    operations = [
        migrations.AddField(
            model_name='capacityassigned',
            name='capacityAvailable',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='capacityassigned',
            name='capacityGap',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='resource',
            name='capacityAssigned',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='resource',
            name='capacityIdle',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='resource',
            name='capacityResource',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='task',
            name='capacityAssigned',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='task',
            name='capacityIdle',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='task',
            name='capacityResource',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='resource',
            name='typeResource',
            field=models.CharField(max_length=20, blank=True, null=True),
        ),
    ]
