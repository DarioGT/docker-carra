# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rqOrgCapacity', '0005_auto_20180803_0941'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='capacityassigned',
            name='capacityAvailable',
        ),
        migrations.RemoveField(
            model_name='capacityassigned',
            name='capacityGap',
        ),
        migrations.AlterField(
            model_name='capacityassigned',
            name='taskSkill',
            field=models.ForeignKey(null=True, blank=True, to='rqOrgCapacity.TaskSkill'),
        ),
    ]
