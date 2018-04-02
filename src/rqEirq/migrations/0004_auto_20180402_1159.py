# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuid
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('protoLib', '0001_initial'),
        ('rqEirq', '0003_auto_20180316_1346'),
    ]

    operations = [
        migrations.CreateModel(
            name='RessourceTech',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('smNaturalCode', models.CharField(null=True, blank=True, editable=False, max_length=50)),
                ('smRegStatus', models.CharField(null=True, blank=True, editable=False, max_length=50)),
                ('smWflowStatus', models.CharField(null=True, blank=True, editable=False, max_length=50)),
                ('smCreatedOn', models.DateTimeField(null=True, auto_now_add=True)),
                ('smModifiedOn', models.DateTimeField(null=True, auto_now=True)),
                ('smUUID', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('ressource', models.ForeignKey(blank=True, to='rqEirq.Responsable', null=True)),
                ('smCreatedBy', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True, editable=False, related_name='+')),
                ('smModifiedBy', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True, editable=False, related_name='+')),
                ('smOwningTeam', models.ForeignKey(blank=True, to='protoLib.TeamHierarchy', null=True, editable=False, related_name='+')),
                ('smOwningUser', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True, editable=False, related_name='+')),
            ],
            options={
                'abstract': False,
                'permissions': (('list_%(class)', 'Can list available %(class)s'),),
            },
        ),
        migrations.CreateModel(
            name='TechChargement',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('smNaturalCode', models.CharField(null=True, blank=True, editable=False, max_length=50)),
                ('smRegStatus', models.CharField(null=True, blank=True, editable=False, max_length=50)),
                ('smWflowStatus', models.CharField(null=True, blank=True, editable=False, max_length=50)),
                ('smCreatedOn', models.DateTimeField(null=True, auto_now_add=True)),
                ('smModifiedOn', models.DateTimeField(null=True, auto_now=True)),
                ('smUUID', models.UUIDField(default=uuid.uuid4, editable=False)),
            ],
            options={
                'abstract': False,
                'permissions': (('list_%(class)', 'Can list available %(class)s'),),
            },
        ),
        migrations.CreateModel(
            name='Technologie',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('smNaturalCode', models.CharField(null=True, blank=True, editable=False, max_length=50)),
                ('smRegStatus', models.CharField(null=True, blank=True, editable=False, max_length=50)),
                ('smWflowStatus', models.CharField(null=True, blank=True, editable=False, max_length=50)),
                ('smCreatedOn', models.DateTimeField(null=True, auto_now_add=True)),
                ('smModifiedOn', models.DateTimeField(null=True, auto_now=True)),
                ('smUUID', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('code', models.CharField(null=True, blank=True, max_length=200)),
                ('label', models.CharField(null=True, blank=True, max_length=200)),
                ('description', models.CharField(null=True, blank=True, max_length=500)),
                ('typeT', models.CharField(null=True, blank=True, max_length=20)),
                ('smCreatedBy', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True, editable=False, related_name='+')),
                ('smModifiedBy', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True, editable=False, related_name='+')),
                ('smOwningTeam', models.ForeignKey(blank=True, to='protoLib.TeamHierarchy', null=True, editable=False, related_name='+')),
                ('smOwningUser', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True, editable=False, related_name='+')),
            ],
            options={
                'abstract': False,
                'permissions': (('list_%(class)', 'Can list available %(class)s'),),
            },
        ),
        migrations.AddField(
            model_name='fichier',
            name='chaineChargement',
            field=models.CharField(null=True, blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='fichier',
            name='chaineExtraction',
            field=models.CharField(null=True, blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='fichier',
            name='chaineNettoyage',
            field=models.CharField(null=True, blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='fichier',
            name='codeUntTraitement',
            field=models.CharField(null=True, blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='fichier',
            name='description',
            field=models.CharField(null=True, blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='fichier',
            name='dgu',
            field=models.CharField(null=True, blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='fichier',
            name='emplacement',
            field=models.CharField(null=True, blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='fichier',
            name='frequence',
            field=models.CharField(null=True, blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='fichier',
            name='notes',
            field=models.CharField(null=True, blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='fichier',
            name='reception',
            field=models.CharField(null=True, blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='fichier',
            name='scenario',
            field=models.CharField(null=True, blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='fichier',
            name='typeExploitation',
            field=models.CharField(null=True, blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='fichier',
            name='typeF',
            field=models.CharField(null=True, blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='fichier',
            name='urlDoc',
            field=models.CharField(null=True, blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='fichier',
            name='urlMeta',
            field=models.CharField(null=True, blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='fichier',
            name='urlModel',
            field=models.CharField(null=True, blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='fichier',
            name='vpa',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='source',
            name='description',
            field=models.CharField(null=True, blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='source',
            name='notes',
            field=models.CharField(null=True, blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='source',
            name='pilote',
            field=models.ForeignKey(blank=True, to='rqEirq.Responsable', null=True, related_name='pilote_set'),
        ),
        migrations.AddField(
            model_name='source',
            name='urlDoc',
            field=models.CharField(null=True, blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='source',
            name='responsable',
            field=models.ForeignKey(blank=True, to='rqEirq.Responsable', null=True, related_name='reposable_set'),
        ),
        migrations.AddField(
            model_name='techchargement',
            name='fichier',
            field=models.ForeignKey(blank=True, to='rqEirq.Fichier', null=True),
        ),
        migrations.AddField(
            model_name='techchargement',
            name='smCreatedBy',
            field=models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True, editable=False, related_name='+'),
        ),
        migrations.AddField(
            model_name='techchargement',
            name='smModifiedBy',
            field=models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True, editable=False, related_name='+'),
        ),
        migrations.AddField(
            model_name='techchargement',
            name='smOwningTeam',
            field=models.ForeignKey(blank=True, to='protoLib.TeamHierarchy', null=True, editable=False, related_name='+'),
        ),
        migrations.AddField(
            model_name='techchargement',
            name='smOwningUser',
            field=models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True, editable=False, related_name='+'),
        ),
        migrations.AddField(
            model_name='techchargement',
            name='technologie',
            field=models.ForeignKey(blank=True, to='rqEirq.Technologie', null=True),
        ),
        migrations.AddField(
            model_name='ressourcetech',
            name='technologie',
            field=models.ForeignKey(blank=True, to='rqEirq.Technologie', null=True),
        ),
    ]
