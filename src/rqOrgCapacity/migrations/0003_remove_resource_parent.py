# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rqOrgCapacity', '0002_auto_20180802_1550'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resource',
            name='parent',
        ),
    ]
