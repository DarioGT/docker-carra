# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rqGraph', '0005_auto_20180830_1406'),
    ]

    operations = [
        migrations.RenameField(
            model_name='node',
            old_name='sytle',
            new_name='style',
        ),
    ]
