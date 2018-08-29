# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rqGraph', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cluster',
            name='parentCluster',
        ),
        migrations.RemoveField(
            model_name='cluster',
            name='smCreatedBy',
        ),
        migrations.RemoveField(
            model_name='cluster',
            name='smModifiedBy',
        ),
        migrations.RemoveField(
            model_name='cluster',
            name='smOwningTeam',
        ),
        migrations.RemoveField(
            model_name='cluster',
            name='smOwningUser',
        ),
        migrations.RemoveField(
            model_name='clusternodes',
            name='cluster',
        ),
        migrations.RemoveField(
            model_name='clusternodes',
            name='node',
        ),
        migrations.RemoveField(
            model_name='clusternodes',
            name='smCreatedBy',
        ),
        migrations.RemoveField(
            model_name='clusternodes',
            name='smModifiedBy',
        ),
        migrations.RemoveField(
            model_name='clusternodes',
            name='smOwningTeam',
        ),
        migrations.RemoveField(
            model_name='clusternodes',
            name='smOwningUser',
        ),
        migrations.RemoveField(
            model_name='canvasdetail',
            name='cluster',
        ),
        migrations.AddField(
            model_name='canvasdetail',
            name='node',
            field=models.ForeignKey(to='rqGraph.Node', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='node',
            name='gvParams',
            field=models.CharField(max_length=800, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='node',
            name='hideNodes',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='node',
            name='isCluster',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='node',
            name='labelAsNode',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='node',
            name='parentNode',
            field=models.ForeignKey(to='rqGraph.Node', blank=True, null=True, related_name='node_set'),
        ),
        migrations.DeleteModel(
            name='Cluster',
        ),
        migrations.DeleteModel(
            name='ClusterNodes',
        ),
        migrations.CreateModel(
            name='Cluster',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('rqGraph.node',),
        ),
    ]
