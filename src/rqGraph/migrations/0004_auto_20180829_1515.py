# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('protoLib', '0001_initial'),
        ('rqGraph', '0003_auto_20180828_1603'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClusterHierarchy',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('smNaturalCode', models.CharField(null=True, blank=True, editable=False, max_length=50)),
                ('smRegStatus', models.CharField(null=True, blank=True, editable=False, max_length=50)),
                ('smWflowStatus', models.CharField(null=True, blank=True, editable=False, max_length=50)),
                ('smCreatedOn', models.DateTimeField(null=True, auto_now_add=True)),
                ('smModifiedOn', models.DateTimeField(null=True, auto_now=True)),
                ('smUUID', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('rankType', models.CharField(null=True, blank=True, max_length=20)),
                ('rank', models.CharField(null=True, blank=True, max_length=200)),
                ('sequence', models.IntegerField(null=True, blank=True)),
                ('container', models.ForeignKey(blank=True, to='rqGraph.Node', related_name='container_set', null=True)),
                ('element', models.ForeignKey(blank=True, to='rqGraph.Node', related_name='element_set', null=True)),
                ('smCreatedBy', models.ForeignKey(blank=True, null=True, to=settings.AUTH_USER_MODEL, related_name='+', editable=False)),
                ('smModifiedBy', models.ForeignKey(blank=True, null=True, to=settings.AUTH_USER_MODEL, related_name='+', editable=False)),
                ('smOwningTeam', models.ForeignKey(blank=True, null=True, to='protoLib.TeamHierarchy', related_name='+', editable=False)),
                ('smOwningUser', models.ForeignKey(blank=True, null=True, to=settings.AUTH_USER_MODEL, related_name='+', editable=False)),
            ],
            options={
                'abstract': False,
                'permissions': (('list_%(class)', 'Can list available %(class)s'),),
            },
        ),
        migrations.RemoveField(
            model_name='canvashierarchy',
            name='container',
        ),
        migrations.RemoveField(
            model_name='canvashierarchy',
            name='element',
        ),
        migrations.RemoveField(
            model_name='canvashierarchy',
            name='smCreatedBy',
        ),
        migrations.RemoveField(
            model_name='canvashierarchy',
            name='smModifiedBy',
        ),
        migrations.RemoveField(
            model_name='canvashierarchy',
            name='smOwningTeam',
        ),
        migrations.RemoveField(
            model_name='canvashierarchy',
            name='smOwningUser',
        ),
        migrations.DeleteModel(
            name='CanvasHierarchy',
        ),
    ]
