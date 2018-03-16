# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import jsonfield2.fields
from django.conf import settings
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('protoLib', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Canvas',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('smNaturalCode', models.CharField(null=True, blank=True, max_length=50, editable=False)),
                ('smRegStatus', models.CharField(null=True, blank=True, max_length=50, editable=False)),
                ('smWflowStatus', models.CharField(null=True, blank=True, max_length=50, editable=False)),
                ('smCreatedOn', models.DateTimeField(null=True, auto_now_add=True)),
                ('smModifiedOn', models.DateTimeField(null=True, auto_now=True)),
                ('smUUID', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('code', models.CharField(null=True, blank=True, max_length=200)),
                ('description', models.CharField(null=True, blank=True, max_length=200)),
                ('smCreatedBy', models.ForeignKey(related_name='+', null=True, blank=True, editable=False, to=settings.AUTH_USER_MODEL)),
                ('smModifiedBy', models.ForeignKey(related_name='+', null=True, blank=True, editable=False, to=settings.AUTH_USER_MODEL)),
                ('smOwningTeam', models.ForeignKey(related_name='+', null=True, blank=True, editable=False, to='protoLib.TeamHierarchy')),
                ('smOwningUser', models.ForeignKey(related_name='+', null=True, blank=True, editable=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
                'permissions': (('list_%(class)', 'Can list available %(class)s'),),
            },
        ),
        migrations.CreateModel(
            name='CanvasDetail',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('smNaturalCode', models.CharField(null=True, blank=True, max_length=50, editable=False)),
                ('smRegStatus', models.CharField(null=True, blank=True, max_length=50, editable=False)),
                ('smWflowStatus', models.CharField(null=True, blank=True, max_length=50, editable=False)),
                ('smCreatedOn', models.DateTimeField(null=True, auto_now_add=True)),
                ('smModifiedOn', models.DateTimeField(null=True, auto_now=True)),
                ('smUUID', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('canvas', models.ForeignKey(null=True, blank=True, to='protoGraph.Canvas')),
            ],
            options={
                'abstract': False,
                'permissions': (('list_%(class)', 'Can list available %(class)s'),),
            },
        ),
        migrations.CreateModel(
            name='Edge',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('smNaturalCode', models.CharField(null=True, blank=True, max_length=50, editable=False)),
                ('smRegStatus', models.CharField(null=True, blank=True, max_length=50, editable=False)),
                ('smWflowStatus', models.CharField(null=True, blank=True, max_length=50, editable=False)),
                ('smCreatedOn', models.DateTimeField(null=True, auto_now_add=True)),
                ('smModifiedOn', models.DateTimeField(null=True, auto_now=True)),
                ('smUUID', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('smInfo', jsonfield2.fields.JSONField(default={})),
                ('code', models.CharField(null=True, blank=True, max_length=200)),
                ('label', models.CharField(null=True, blank=True, max_length=200)),
                ('description', models.CharField(null=True, blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='EdgeCategory',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('smNaturalCode', models.CharField(null=True, blank=True, max_length=50, editable=False)),
                ('smRegStatus', models.CharField(null=True, blank=True, max_length=50, editable=False)),
                ('smWflowStatus', models.CharField(null=True, blank=True, max_length=50, editable=False)),
                ('smCreatedOn', models.DateTimeField(null=True, auto_now_add=True)),
                ('smModifiedOn', models.DateTimeField(null=True, auto_now=True)),
                ('smUUID', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('smInfo', jsonfield2.fields.JSONField(default={})),
                ('code', models.CharField(null=True, blank=True, max_length=200)),
                ('description', models.CharField(null=True, blank=True, max_length=200)),
                ('smCreatedBy', models.ForeignKey(related_name='+', null=True, blank=True, editable=False, to=settings.AUTH_USER_MODEL)),
                ('smModifiedBy', models.ForeignKey(related_name='+', null=True, blank=True, editable=False, to=settings.AUTH_USER_MODEL)),
                ('smOwningTeam', models.ForeignKey(related_name='+', null=True, blank=True, editable=False, to='protoLib.TeamHierarchy')),
                ('smOwningUser', models.ForeignKey(related_name='+', null=True, blank=True, editable=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Node',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('smNaturalCode', models.CharField(null=True, blank=True, max_length=50, editable=False)),
                ('smRegStatus', models.CharField(null=True, blank=True, max_length=50, editable=False)),
                ('smWflowStatus', models.CharField(null=True, blank=True, max_length=50, editable=False)),
                ('smCreatedOn', models.DateTimeField(null=True, auto_now_add=True)),
                ('smModifiedOn', models.DateTimeField(null=True, auto_now=True)),
                ('smUUID', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('smInfo', jsonfield2.fields.JSONField(default={})),
                ('code', models.CharField(null=True, blank=True, max_length=200)),
                ('label', models.CharField(null=True, blank=True, max_length=200)),
                ('description', models.CharField(null=True, blank=True, max_length=200)),
                ('idSource', models.IntegerField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='NodeCategory',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('smNaturalCode', models.CharField(null=True, blank=True, max_length=50, editable=False)),
                ('smRegStatus', models.CharField(null=True, blank=True, max_length=50, editable=False)),
                ('smWflowStatus', models.CharField(null=True, blank=True, max_length=50, editable=False)),
                ('smCreatedOn', models.DateTimeField(null=True, auto_now_add=True)),
                ('smModifiedOn', models.DateTimeField(null=True, auto_now=True)),
                ('smUUID', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('smInfo', jsonfield2.fields.JSONField(default={})),
                ('code', models.CharField(null=True, blank=True, max_length=200)),
                ('description', models.CharField(null=True, blank=True, max_length=200)),
                ('smCreatedBy', models.ForeignKey(related_name='+', null=True, blank=True, editable=False, to=settings.AUTH_USER_MODEL)),
                ('smModifiedBy', models.ForeignKey(related_name='+', null=True, blank=True, editable=False, to=settings.AUTH_USER_MODEL)),
                ('smOwningTeam', models.ForeignKey(related_name='+', null=True, blank=True, editable=False, to='protoLib.TeamHierarchy')),
                ('smOwningUser', models.ForeignKey(related_name='+', null=True, blank=True, editable=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='node',
            name='category',
            field=models.ForeignKey(null=True, blank=True, to='protoGraph.NodeCategory'),
        ),
        migrations.AddField(
            model_name='node',
            name='smCreatedBy',
            field=models.ForeignKey(related_name='+', null=True, blank=True, editable=False, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='node',
            name='smModifiedBy',
            field=models.ForeignKey(related_name='+', null=True, blank=True, editable=False, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='node',
            name='smOwningTeam',
            field=models.ForeignKey(related_name='+', null=True, blank=True, editable=False, to='protoLib.TeamHierarchy'),
        ),
        migrations.AddField(
            model_name='node',
            name='smOwningUser',
            field=models.ForeignKey(related_name='+', null=True, blank=True, editable=False, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='edge',
            name='category',
            field=models.ForeignKey(null=True, blank=True, to='protoGraph.EdgeCategory'),
        ),
        migrations.AddField(
            model_name='edge',
            name='node0',
            field=models.ForeignKey(null=True, blank=True, related_name='node0_set', to='protoGraph.Node'),
        ),
        migrations.AddField(
            model_name='edge',
            name='node1',
            field=models.ForeignKey(null=True, blank=True, related_name='node1_set', to='protoGraph.Node'),
        ),
        migrations.AddField(
            model_name='edge',
            name='smCreatedBy',
            field=models.ForeignKey(related_name='+', null=True, blank=True, editable=False, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='edge',
            name='smModifiedBy',
            field=models.ForeignKey(related_name='+', null=True, blank=True, editable=False, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='edge',
            name='smOwningTeam',
            field=models.ForeignKey(related_name='+', null=True, blank=True, editable=False, to='protoLib.TeamHierarchy'),
        ),
        migrations.AddField(
            model_name='edge',
            name='smOwningUser',
            field=models.ForeignKey(related_name='+', null=True, blank=True, editable=False, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='canvasdetail',
            name='edge',
            field=models.ForeignKey(null=True, blank=True, to='protoGraph.Edge'),
        ),
        migrations.AddField(
            model_name='canvasdetail',
            name='smCreatedBy',
            field=models.ForeignKey(related_name='+', null=True, blank=True, editable=False, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='canvasdetail',
            name='smModifiedBy',
            field=models.ForeignKey(related_name='+', null=True, blank=True, editable=False, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='canvasdetail',
            name='smOwningTeam',
            field=models.ForeignKey(related_name='+', null=True, blank=True, editable=False, to='protoLib.TeamHierarchy'),
        ),
        migrations.AddField(
            model_name='canvasdetail',
            name='smOwningUser',
            field=models.ForeignKey(related_name='+', null=True, blank=True, editable=False, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='node',
            unique_together=set([('code', 'category')]),
        ),
        migrations.AlterUniqueTogether(
            name='edge',
            unique_together=set([('code', 'node0', 'node1')]),
        ),
    ]
