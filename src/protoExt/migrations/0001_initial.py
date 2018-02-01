# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import uuid
import jsonfield2.fields


class Migration(migrations.Migration):

    dependencies = [
        ('protoLib', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomDefinition',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('smNaturalCode', models.CharField(blank=True, max_length=50, null=True, editable=False)),
                ('smRegStatus', models.CharField(blank=True, max_length=50, null=True, editable=False)),
                ('smWflowStatus', models.CharField(blank=True, max_length=50, null=True, editable=False)),
                ('smCreatedOn', models.DateTimeField(auto_now_add=True, null=True)),
                ('smModifiedOn', models.DateTimeField(null=True, auto_now=True)),
                ('smUUID', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('code', models.CharField(max_length=200)),
                ('description', models.TextField(verbose_name='Descriptions', blank=True, null=True)),
                ('active', models.BooleanField(default=True)),
                ('overWrite', models.BooleanField(default=False)),
                ('metaDefinition', jsonfield2.fields.JSONField(default={})),
                ('smCreatedBy', models.ForeignKey(blank=True, editable=False, null=True, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('smModifiedBy', models.ForeignKey(blank=True, editable=False, null=True, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('smOwningTeam', models.ForeignKey(blank=True, editable=False, null=True, related_name='+', to='protoLib.TeamHierarchy')),
                ('smOwningUser', models.ForeignKey(blank=True, editable=False, null=True, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Parameters',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('smNaturalCode', models.CharField(blank=True, max_length=50, null=True, editable=False)),
                ('smRegStatus', models.CharField(blank=True, max_length=50, null=True, editable=False)),
                ('smWflowStatus', models.CharField(blank=True, max_length=50, null=True, editable=False)),
                ('smCreatedOn', models.DateTimeField(auto_now_add=True, null=True)),
                ('smModifiedOn', models.DateTimeField(null=True, auto_now=True)),
                ('smUUID', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('smInfo', jsonfield2.fields.JSONField(default={})),
                ('parameterKey', models.CharField(max_length=250)),
                ('parameterTag', models.CharField(blank=True, max_length=250, null=True)),
                ('parameterValue', models.CharField(max_length=250)),
                ('smCreatedBy', models.ForeignKey(blank=True, editable=False, null=True, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('smModifiedBy', models.ForeignKey(blank=True, editable=False, null=True, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('smOwningTeam', models.ForeignKey(blank=True, editable=False, null=True, related_name='+', to='protoLib.TeamHierarchy')),
                ('smOwningUser', models.ForeignKey(blank=True, editable=False, null=True, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ViewDefinition',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('code', models.CharField(max_length=200, unique=True)),
                ('description', models.TextField(verbose_name='Description', blank=True, null=True)),
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
