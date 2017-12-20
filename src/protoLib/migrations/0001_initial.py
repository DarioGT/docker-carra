# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import jsonfield2.fields
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ContextEntity',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('smNaturalCode', models.CharField(blank=True, max_length=50, editable=False, null=True)),
                ('smRegStatus', models.CharField(blank=True, max_length=50, editable=False, null=True)),
                ('smWflowStatus', models.CharField(blank=True, max_length=50, editable=False, null=True)),
                ('smCreatedOn', models.DateTimeField(auto_now_add=True, null=True)),
                ('smModifiedOn', models.DateTimeField(auto_now=True, null=True)),
                ('smUUID', models.UUIDField(editable=False, default=uuid.uuid4)),
                ('propName', models.CharField(null=True, max_length=200, blank=True, default='')),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='ContextUser',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('smNaturalCode', models.CharField(blank=True, max_length=50, editable=False, null=True)),
                ('smRegStatus', models.CharField(blank=True, max_length=50, editable=False, null=True)),
                ('smWflowStatus', models.CharField(blank=True, max_length=50, editable=False, null=True)),
                ('smCreatedOn', models.DateTimeField(auto_now_add=True, null=True)),
                ('smModifiedOn', models.DateTimeField(auto_now=True, null=True)),
                ('smUUID', models.UUIDField(editable=False, default=uuid.uuid4)),
                ('propValue', models.CharField(null=True, max_length=200, blank=True)),
                ('description', models.TextField(null=True, blank=True)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='ContextVar',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('smNaturalCode', models.CharField(blank=True, max_length=50, editable=False, null=True)),
                ('smRegStatus', models.CharField(blank=True, max_length=50, editable=False, null=True)),
                ('smWflowStatus', models.CharField(blank=True, max_length=50, editable=False, null=True)),
                ('smCreatedOn', models.DateTimeField(auto_now_add=True, null=True)),
                ('smModifiedOn', models.DateTimeField(auto_now=True, null=True)),
                ('smUUID', models.UUIDField(editable=False, default=uuid.uuid4)),
                ('propName', models.CharField(max_length=500, default='id')),
                ('description', models.TextField(null=True, blank=True)),
                ('modelCType', models.ForeignKey(to='contenttypes.ContentType')),
                ('smCreatedBy', models.ForeignKey(to=settings.AUTH_USER_MODEL, editable=False, null=True, blank=True, related_name='+')),
                ('smModifiedBy', models.ForeignKey(to=settings.AUTH_USER_MODEL, editable=False, null=True, blank=True, related_name='+')),
            ],
        ),
        migrations.CreateModel(
            name='EntityMap',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('entityConfig', jsonfield2.fields.JSONField(default={})),
                ('entityBase', models.OneToOneField(to='contenttypes.ContentType')),
            ],
        ),
        migrations.CreateModel(
            name='Logger',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('smCreatedOn', models.DateTimeField(auto_now=True, null=True)),
                ('logType', models.CharField(max_length=10, default='INF')),
                ('logObject', models.CharField(null=True, max_length=250, blank=True)),
                ('logNotes', models.CharField(null=True, max_length=250, blank=True)),
                ('logInfo', models.TextField(null=True, blank=True)),
                ('logKey', models.CharField(max_length=5, default='', choices=[('INF', 'INFO'), ('WAR', 'WARNING'), ('ERR', 'ERROR'), ('INS', 'INSERT'), ('UPD', 'UPDATE'), ('DEL', 'DELETE')])),
                ('smCreatedBy', models.ForeignKey(to=settings.AUTH_USER_MODEL, editable=False, null=True, blank=True, related_name='+')),
            ],
        ),
        migrations.CreateModel(
            name='ProtoVersionTitle',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('smNaturalCode', models.CharField(blank=True, max_length=50, editable=False, null=True)),
                ('smRegStatus', models.CharField(blank=True, max_length=50, editable=False, null=True)),
                ('smWflowStatus', models.CharField(blank=True, max_length=50, editable=False, null=True)),
                ('smCreatedOn', models.DateTimeField(auto_now_add=True, null=True)),
                ('smModifiedOn', models.DateTimeField(auto_now=True, null=True)),
                ('smUUID', models.UUIDField(editable=False, default=uuid.uuid4)),
                ('versionCode', models.CharField(null=True, max_length=50, blank=True, default='0')),
                ('description', models.TextField(null=True, verbose_name='Descriptions', blank=True)),
                ('active', models.BooleanField(default=True)),
                ('smCreatedBy', models.ForeignKey(to=settings.AUTH_USER_MODEL, editable=False, null=True, blank=True, related_name='+')),
                ('smModifiedBy', models.ForeignKey(to=settings.AUTH_USER_MODEL, editable=False, null=True, blank=True, related_name='+')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TeamHierarchy',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('code', models.CharField(max_length=200, unique=True)),
                ('description', models.TextField(null=True, verbose_name='Descriptions', blank=True)),
                ('site', models.IntegerField(null=True, blank=True)),
                ('parentNode', models.ForeignKey(to='protoLib.TeamHierarchy', related_name='downHierachy', null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('language', models.CharField(null=True, max_length=500, blank=True)),
                ('userTree', models.CharField(null=True, max_length=500, blank=True)),
                ('userConfig', jsonfield2.fields.JSONField(default={})),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
                ('userTeam', models.ForeignKey(to='protoLib.TeamHierarchy', related_name='userTeam', null=True, blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='protoversiontitle',
            name='smOwningTeam',
            field=models.ForeignKey(to='protoLib.TeamHierarchy', editable=False, null=True, blank=True, related_name='+'),
        ),
        migrations.AddField(
            model_name='protoversiontitle',
            name='smOwningUser',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, editable=False, null=True, blank=True, related_name='+'),
        ),
        migrations.AddField(
            model_name='protoversiontitle',
            name='versionBase',
            field=models.ForeignKey(to='protoLib.ProtoVersionTitle', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='logger',
            name='smOwningTeam',
            field=models.ForeignKey(to='protoLib.TeamHierarchy', editable=False, null=True, blank=True, related_name='+'),
        ),
        migrations.AddField(
            model_name='contextvar',
            name='smOwningTeam',
            field=models.ForeignKey(to='protoLib.TeamHierarchy', editable=False, null=True, blank=True, related_name='+'),
        ),
        migrations.AddField(
            model_name='contextvar',
            name='smOwningUser',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, editable=False, null=True, blank=True, related_name='+'),
        ),
        migrations.AddField(
            model_name='contextuser',
            name='contextVar',
            field=models.ForeignKey(to='protoLib.ContextVar'),
        ),
        migrations.AddField(
            model_name='contextuser',
            name='smCreatedBy',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, editable=False, null=True, blank=True, related_name='+'),
        ),
        migrations.AddField(
            model_name='contextuser',
            name='smModifiedBy',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, editable=False, null=True, blank=True, related_name='+'),
        ),
        migrations.AddField(
            model_name='contextuser',
            name='smOwningTeam',
            field=models.ForeignKey(to='protoLib.TeamHierarchy', editable=False, null=True, blank=True, related_name='+'),
        ),
        migrations.AddField(
            model_name='contextuser',
            name='smOwningUser',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, editable=False, null=True, blank=True, related_name='+'),
        ),
        migrations.AddField(
            model_name='contextentity',
            name='contextVar',
            field=models.ForeignKey(to='protoLib.ContextVar'),
        ),
        migrations.AddField(
            model_name='contextentity',
            name='entity',
            field=models.ForeignKey(to='contenttypes.ContentType'),
        ),
        migrations.AddField(
            model_name='contextentity',
            name='smCreatedBy',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, editable=False, null=True, blank=True, related_name='+'),
        ),
        migrations.AddField(
            model_name='contextentity',
            name='smModifiedBy',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, editable=False, null=True, blank=True, related_name='+'),
        ),
        migrations.AddField(
            model_name='contextentity',
            name='smOwningTeam',
            field=models.ForeignKey(to='protoLib.TeamHierarchy', editable=False, null=True, blank=True, related_name='+'),
        ),
        migrations.AddField(
            model_name='contextentity',
            name='smOwningUser',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, editable=False, null=True, blank=True, related_name='+'),
        ),
        migrations.AlterUniqueTogether(
            name='contextvar',
            unique_together=set([('modelCType', 'propName')]),
        ),
        migrations.AlterUniqueTogether(
            name='contextuser',
            unique_together=set([('contextVar', 'smOwningUser')]),
        ),
        migrations.AlterUniqueTogether(
            name='contextentity',
            unique_together=set([('contextVar', 'entity')]),
        ),
    ]
