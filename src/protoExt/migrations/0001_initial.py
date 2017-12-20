# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import jsonfield2.fields
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('protoLib', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomDefinition',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('smNaturalCode', models.CharField(max_length=50, editable=False, null=True, blank=True)),
                ('smRegStatus', models.CharField(max_length=50, editable=False, null=True, blank=True)),
                ('smWflowStatus', models.CharField(max_length=50, editable=False, null=True, blank=True)),
                ('smCreatedOn', models.DateTimeField(auto_now_add=True, null=True)),
                ('smModifiedOn', models.DateTimeField(auto_now=True, null=True)),
                ('smUUID', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('code', models.CharField(max_length=200)),
                ('description', models.TextField(null=True, blank=True, verbose_name='Descriptions')),
                ('active', models.BooleanField(default=True)),
                ('overWrite', models.BooleanField(default=False)),
                ('metaDefinition', jsonfield2.fields.JSONField(default={})),
                ('smCreatedBy', models.ForeignKey(related_name='+', editable=False, blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('smModifiedBy', models.ForeignKey(related_name='+', editable=False, blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('smOwningTeam', models.ForeignKey(related_name='+', editable=False, blank=True, to='protoLib.TeamHierarchy', null=True)),
                ('smOwningUser', models.ForeignKey(related_name='+', editable=False, blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Parameters',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('smNaturalCode', models.CharField(max_length=50, editable=False, null=True, blank=True)),
                ('smRegStatus', models.CharField(max_length=50, editable=False, null=True, blank=True)),
                ('smWflowStatus', models.CharField(max_length=50, editable=False, null=True, blank=True)),
                ('smCreatedOn', models.DateTimeField(auto_now_add=True, null=True)),
                ('smModifiedOn', models.DateTimeField(auto_now=True, null=True)),
                ('smUUID', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('smInfo', jsonfield2.fields.JSONField(default={})),
                ('parameterKey', models.CharField(max_length=250)),
                ('parameterTag', models.CharField(max_length=250, null=True, blank=True)),
                ('parameterValue', models.CharField(max_length=250)),
                ('smCreatedBy', models.ForeignKey(related_name='+', editable=False, blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('smModifiedBy', models.ForeignKey(related_name='+', editable=False, blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('smOwningTeam', models.ForeignKey(related_name='+', editable=False, blank=True, to='protoLib.TeamHierarchy', null=True)),
                ('smOwningUser', models.ForeignKey(related_name='+', editable=False, blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ViewDefinition',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('code', models.CharField(max_length=200, unique=True)),
                ('description', models.TextField(null=True, blank=True, verbose_name='Description')),
                ('active', models.BooleanField(default=True)),
                ('overWrite', models.BooleanField(default=False)),
                ('metaDefinition', jsonfield2.fields.JSONField(default={})),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='customdefinition',
            unique_together=set([('code', 'smOwningUser')]),
        ),
    ]
