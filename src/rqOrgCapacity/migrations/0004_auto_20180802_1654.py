# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rqOrgCapacity', '0003_remove_resource_parent'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='responsable',
            new_name='resource',
        ),
    ]
