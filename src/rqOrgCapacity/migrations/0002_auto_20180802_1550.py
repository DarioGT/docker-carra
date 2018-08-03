# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rqOrgCapacity', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='capacityassigned',
            name='capacityAssigned',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='resourceskill',
            name='capacityAssigned',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='resourceskill',
            name='capacityIdle',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='resourceskill',
            name='capacityResource',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='taskskill',
            name='capacityAssigned',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='taskskill',
            name='capacityAvailable',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='taskskill',
            name='capacityGap',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='taskskill',
            name='capacityNeed',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
