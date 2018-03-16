# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rqEirq', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dependance',
            name='source',
        ),
        migrations.AddField(
            model_name='dependance',
            name='fichier',
            field=models.ForeignKey(null=True, blank=True, to='rqEirq.Fichier'),
        ),
        migrations.AlterField(
            model_name='dependance',
            name='produit',
            field=models.ForeignKey(null=True, blank=True, to='rqEirq.Source'),
        ),
    ]
