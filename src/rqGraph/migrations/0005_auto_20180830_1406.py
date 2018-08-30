# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rqGraph', '0004_auto_20180829_1515'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='edgestyle',
            name='arrowhead',
        ),
        migrations.RemoveField(
            model_name='edgestyle',
            name='arrowsize',
        ),
        migrations.RemoveField(
            model_name='edgestyle',
            name='arrowtail',
        ),
        migrations.RemoveField(
            model_name='edgestyle',
            name='color',
        ),
        migrations.RemoveField(
            model_name='edgestyle',
            name='constraint',
        ),
        migrations.RemoveField(
            model_name='edgestyle',
            name='dir',
        ),
        migrations.RemoveField(
            model_name='edgestyle',
            name='fontcolor',
        ),
        migrations.RemoveField(
            model_name='edgestyle',
            name='fontname',
        ),
        migrations.RemoveField(
            model_name='edgestyle',
            name='fontsize',
        ),
        migrations.RemoveField(
            model_name='edgestyle',
            name='lhead',
        ),
        migrations.RemoveField(
            model_name='edgestyle',
            name='ltail',
        ),
        migrations.RemoveField(
            model_name='edgestyle',
            name='style',
        ),
        migrations.RemoveField(
            model_name='edgestyle',
            name='xlabel',
        ),
        migrations.RemoveField(
            model_name='nodestyle',
            name='color',
        ),
        migrations.RemoveField(
            model_name='nodestyle',
            name='fillcolor',
        ),
        migrations.RemoveField(
            model_name='nodestyle',
            name='fixedsize',
        ),
        migrations.RemoveField(
            model_name='nodestyle',
            name='fontcolor',
        ),
        migrations.RemoveField(
            model_name='nodestyle',
            name='fontname',
        ),
        migrations.RemoveField(
            model_name='nodestyle',
            name='fontsize',
        ),
        migrations.RemoveField(
            model_name='nodestyle',
            name='gradientangle',
        ),
        migrations.RemoveField(
            model_name='nodestyle',
            name='height',
        ),
        migrations.RemoveField(
            model_name='nodestyle',
            name='imagePath',
        ),
        migrations.RemoveField(
            model_name='nodestyle',
            name='shape',
        ),
        migrations.RemoveField(
            model_name='nodestyle',
            name='style',
        ),
        migrations.RemoveField(
            model_name='nodestyle',
            name='width',
        ),
        migrations.AlterField(
            model_name='clusterhierarchy',
            name='container',
            field=models.ForeignKey(related_name='container_set', to='rqGraph.Node'),
        ),
        migrations.AlterField(
            model_name='clusterhierarchy',
            name='element',
            field=models.ForeignKey(related_name='element_set', to='rqGraph.Node'),
        ),
    ]
