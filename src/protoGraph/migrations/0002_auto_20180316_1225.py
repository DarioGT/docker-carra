# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('protoGraph', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='edge',
            unique_together=set([('node0', 'node1')]),
        ),
        migrations.AlterUniqueTogether(
            name='node',
            unique_together=set([('idSource', 'category')]),
        ),
    ]
