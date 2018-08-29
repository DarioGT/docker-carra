# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuid
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('protoLib', '0001_initial'),
        ('rqGraph', '0002_auto_20180828_1406'),
    ]

    operations = [
        migrations.CreateModel(
            name='CanvasHierarchy',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('smNaturalCode', models.CharField(null=True, editable=False, blank=True, max_length=50)),
                ('smRegStatus', models.CharField(null=True, editable=False, blank=True, max_length=50)),
                ('smWflowStatus', models.CharField(null=True, editable=False, blank=True, max_length=50)),
                ('smCreatedOn', models.DateTimeField(null=True, auto_now_add=True)),
                ('smModifiedOn', models.DateTimeField(null=True, auto_now=True)),
                ('smUUID', models.UUIDField(editable=False, default=uuid.uuid4)),
                ('rankType', models.CharField(null=True, blank=True, max_length=20)),
                ('rank', models.CharField(null=True, blank=True, max_length=200)),
            ],
            options={
                'permissions': (('list_%(class)', 'Can list available %(class)s'),),
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='canvas',
            name='smCreatedBy',
        ),
        migrations.RemoveField(
            model_name='canvas',
            name='smModifiedBy',
        ),
        migrations.RemoveField(
            model_name='canvas',
            name='smOwningTeam',
        ),
        migrations.RemoveField(
            model_name='canvas',
            name='smOwningUser',
        ),
        migrations.RemoveField(
            model_name='canvasdetail',
            name='canvas',
        ),
        migrations.RemoveField(
            model_name='canvasdetail',
            name='node',
        ),
        migrations.RemoveField(
            model_name='canvasdetail',
            name='smCreatedBy',
        ),
        migrations.RemoveField(
            model_name='canvasdetail',
            name='smModifiedBy',
        ),
        migrations.RemoveField(
            model_name='canvasdetail',
            name='smOwningTeam',
        ),
        migrations.RemoveField(
            model_name='canvasdetail',
            name='smOwningUser',
        ),
        migrations.CreateModel(
            name='NodeLink',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('rqGraph.node',),
        ),
        migrations.RemoveField(
            model_name='node',
            name='parentNode',
        ),
        migrations.RemoveField(
            model_name='node',
            name='rank',
        ),
        migrations.AlterField(
            model_name='node',
            name='isCluster',
            field=models.BooleanField(default=False),
        ),
        migrations.DeleteModel(
            name='Canvas',
        ),
        migrations.DeleteModel(
            name='CanvasDetail',
        ),
        migrations.AddField(
            model_name='canvashierarchy',
            name='container',
            field=models.ForeignKey(to='rqGraph.Node', null=True, blank=True, related_name='container_set'),
        ),
        migrations.AddField(
            model_name='canvashierarchy',
            name='element',
            field=models.ForeignKey(to='rqGraph.Node', null=True, blank=True, related_name='element_set'),
        ),
        migrations.AddField(
            model_name='canvashierarchy',
            name='smCreatedBy',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True, editable=False, blank=True, related_name='+'),
        ),
        migrations.AddField(
            model_name='canvashierarchy',
            name='smModifiedBy',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True, editable=False, blank=True, related_name='+'),
        ),
        migrations.AddField(
            model_name='canvashierarchy',
            name='smOwningTeam',
            field=models.ForeignKey(to='protoLib.TeamHierarchy', null=True, editable=False, blank=True, related_name='+'),
        ),
        migrations.AddField(
            model_name='canvashierarchy',
            name='smOwningUser',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True, editable=False, blank=True, related_name='+'),
        ),
    ]
