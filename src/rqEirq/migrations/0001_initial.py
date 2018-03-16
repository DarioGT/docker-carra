# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('protoLib', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Dependance',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('smNaturalCode', models.CharField(blank=True, editable=False, max_length=50, null=True)),
                ('smRegStatus', models.CharField(blank=True, editable=False, max_length=50, null=True)),
                ('smWflowStatus', models.CharField(blank=True, editable=False, max_length=50, null=True)),
                ('smCreatedOn', models.DateTimeField(auto_now_add=True, null=True)),
                ('smModifiedOn', models.DateTimeField(auto_now=True, null=True)),
                ('smUUID', models.UUIDField(editable=False, default=uuid.uuid4)),
            ],
            options={
                'permissions': (('list_%(class)', 'Can list available %(class)s'),),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Fichier',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('smNaturalCode', models.CharField(blank=True, editable=False, max_length=50, null=True)),
                ('smRegStatus', models.CharField(blank=True, editable=False, max_length=50, null=True)),
                ('smWflowStatus', models.CharField(blank=True, editable=False, max_length=50, null=True)),
                ('smCreatedOn', models.DateTimeField(auto_now_add=True, null=True)),
                ('smModifiedOn', models.DateTimeField(auto_now=True, null=True)),
                ('smUUID', models.UUIDField(editable=False, default=uuid.uuid4)),
                ('code', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'permissions': (('list_%(class)', 'Can list available %(class)s'),),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Responsable',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('smNaturalCode', models.CharField(blank=True, editable=False, max_length=50, null=True)),
                ('smRegStatus', models.CharField(blank=True, editable=False, max_length=50, null=True)),
                ('smWflowStatus', models.CharField(blank=True, editable=False, max_length=50, null=True)),
                ('smCreatedOn', models.DateTimeField(auto_now_add=True, null=True)),
                ('smModifiedOn', models.DateTimeField(auto_now=True, null=True)),
                ('smUUID', models.UUIDField(editable=False, default=uuid.uuid4)),
                ('code', models.CharField(blank=True, max_length=200, null=True)),
                ('coordonnees', models.CharField(blank=True, max_length=200, null=True)),
                ('notes', models.CharField(blank=True, max_length=200, null=True)),
                ('smCreatedBy', models.ForeignKey(blank=True, editable=False, related_name='+', null=True, to=settings.AUTH_USER_MODEL)),
                ('smModifiedBy', models.ForeignKey(blank=True, editable=False, related_name='+', null=True, to=settings.AUTH_USER_MODEL)),
                ('smOwningTeam', models.ForeignKey(blank=True, editable=False, related_name='+', null=True, to='protoLib.TeamHierarchy')),
                ('smOwningUser', models.ForeignKey(blank=True, editable=False, related_name='+', null=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'permissions': (('list_%(class)', 'Can list available %(class)s'),),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('smNaturalCode', models.CharField(blank=True, editable=False, max_length=50, null=True)),
                ('smRegStatus', models.CharField(blank=True, editable=False, max_length=50, null=True)),
                ('smWflowStatus', models.CharField(blank=True, editable=False, max_length=50, null=True)),
                ('smCreatedOn', models.DateTimeField(auto_now_add=True, null=True)),
                ('smModifiedOn', models.DateTimeField(auto_now=True, null=True)),
                ('smUUID', models.UUIDField(editable=False, default=uuid.uuid4)),
                ('code', models.CharField(blank=True, max_length=200, null=True)),
                ('typeSource', models.CharField(choices=[('INTERNE', 'Int'), ('EXTERNE', 'Ext'), ('ACHAT', 'Achat'), ('FEDERAL', 'Fédéral'), ('PRODUIT', 'Produit'), ('REF', 'Référentiel')], blank=True, max_length=20, null=True)),
                ('responsable', models.ForeignKey(blank=True, null=True, to='rqEirq.Responsable')),
                ('smCreatedBy', models.ForeignKey(blank=True, editable=False, related_name='+', null=True, to=settings.AUTH_USER_MODEL)),
                ('smModifiedBy', models.ForeignKey(blank=True, editable=False, related_name='+', null=True, to=settings.AUTH_USER_MODEL)),
                ('smOwningTeam', models.ForeignKey(blank=True, editable=False, related_name='+', null=True, to='protoLib.TeamHierarchy')),
                ('smOwningUser', models.ForeignKey(blank=True, editable=False, related_name='+', null=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'permissions': (('list_%(class)', 'Can list available %(class)s'),),
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='fichier',
            name='responsable',
            field=models.ForeignKey(blank=True, null=True, to='rqEirq.Responsable'),
        ),
        migrations.AddField(
            model_name='fichier',
            name='smCreatedBy',
            field=models.ForeignKey(blank=True, editable=False, related_name='+', null=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='fichier',
            name='smModifiedBy',
            field=models.ForeignKey(blank=True, editable=False, related_name='+', null=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='fichier',
            name='smOwningTeam',
            field=models.ForeignKey(blank=True, editable=False, related_name='+', null=True, to='protoLib.TeamHierarchy'),
        ),
        migrations.AddField(
            model_name='fichier',
            name='smOwningUser',
            field=models.ForeignKey(blank=True, editable=False, related_name='+', null=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='fichier',
            name='source',
            field=models.ForeignKey(blank=True, null=True, to='rqEirq.Source'),
        ),
        migrations.AddField(
            model_name='dependance',
            name='produit',
            field=models.ForeignKey(blank=True, related_name='produit_set', null=True, to='rqEirq.Source'),
        ),
        migrations.AddField(
            model_name='dependance',
            name='smCreatedBy',
            field=models.ForeignKey(blank=True, editable=False, related_name='+', null=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='dependance',
            name='smModifiedBy',
            field=models.ForeignKey(blank=True, editable=False, related_name='+', null=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='dependance',
            name='smOwningTeam',
            field=models.ForeignKey(blank=True, editable=False, related_name='+', null=True, to='protoLib.TeamHierarchy'),
        ),
        migrations.AddField(
            model_name='dependance',
            name='smOwningUser',
            field=models.ForeignKey(blank=True, editable=False, related_name='+', null=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='dependance',
            name='source',
            field=models.ForeignKey(blank=True, related_name='source_set', null=True, to='rqEirq.Source'),
        ),
    ]
