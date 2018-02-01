# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import jsonfield2.fields
import taggit.managers
from django.conf import settings
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
        ('protoLib', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Diagram',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('smNaturalCode', models.CharField(editable=False, blank=True, null=True, max_length=50)),
                ('smRegStatus', models.CharField(editable=False, blank=True, null=True, max_length=50)),
                ('smWflowStatus', models.CharField(editable=False, blank=True, null=True, max_length=50)),
                ('smCreatedOn', models.DateTimeField(null=True, auto_now_add=True)),
                ('smModifiedOn', models.DateTimeField(null=True, auto_now=True)),
                ('smUUID', models.UUIDField(editable=False, default=uuid.uuid4)),
                ('smInfo', jsonfield2.fields.JSONField(default={})),
                ('code', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, null=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('title', models.CharField(max_length=100, blank=True, null=True)),
                ('prefix', models.CharField(max_length=20, blank=True, null=True)),
                ('graphLevel', models.IntegerField(blank=True, null=True, default=0)),
                ('grphMode', models.IntegerField(blank=True, null=True, default=0)),
                ('graphForm', models.IntegerField(blank=True, null=True, default=0)),
                ('showPrpType', models.BooleanField(default=False)),
                ('showBorder', models.BooleanField(default=False)),
                ('showFKey', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='DiagramEntity',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('smNaturalCode', models.CharField(editable=False, blank=True, null=True, max_length=50)),
                ('smRegStatus', models.CharField(editable=False, blank=True, null=True, max_length=50)),
                ('smWflowStatus', models.CharField(editable=False, blank=True, null=True, max_length=50)),
                ('smCreatedOn', models.DateTimeField(null=True, auto_now_add=True)),
                ('smModifiedOn', models.DateTimeField(null=True, auto_now=True)),
                ('smUUID', models.UUIDField(editable=False, default=uuid.uuid4)),
                ('smInfo', jsonfield2.fields.JSONField(default={})),
                ('info', jsonfield2.fields.JSONField(default={})),
                ('diagram', models.ForeignKey(to='prototype.Diagram')),
            ],
        ),
        migrations.CreateModel(
            name='Entity',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('smNaturalCode', models.CharField(editable=False, blank=True, null=True, max_length=50)),
                ('smRegStatus', models.CharField(editable=False, blank=True, null=True, max_length=50)),
                ('smWflowStatus', models.CharField(editable=False, blank=True, null=True, max_length=50)),
                ('smCreatedOn', models.DateTimeField(null=True, auto_now_add=True)),
                ('smModifiedOn', models.DateTimeField(null=True, auto_now=True)),
                ('smUUID', models.UUIDField(editable=False, default=uuid.uuid4)),
                ('smInfo', jsonfield2.fields.JSONField(default={})),
                ('code', models.CharField(max_length=200)),
                ('dbName', models.CharField(max_length=200, blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Model',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('smNaturalCode', models.CharField(editable=False, blank=True, null=True, max_length=50)),
                ('smRegStatus', models.CharField(editable=False, blank=True, null=True, max_length=50)),
                ('smWflowStatus', models.CharField(editable=False, blank=True, null=True, max_length=50)),
                ('smCreatedOn', models.DateTimeField(null=True, auto_now_add=True)),
                ('smModifiedOn', models.DateTimeField(null=True, auto_now=True)),
                ('smUUID', models.UUIDField(editable=False, default=uuid.uuid4)),
                ('smInfo', jsonfield2.fields.JSONField(default={})),
                ('code', models.CharField(max_length=200)),
                ('category', models.CharField(max_length=50, blank=True, null=True)),
                ('modelPrefix', models.CharField(max_length=50, blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('smNaturalCode', models.CharField(editable=False, blank=True, null=True, max_length=50)),
                ('smRegStatus', models.CharField(editable=False, blank=True, null=True, max_length=50)),
                ('smWflowStatus', models.CharField(editable=False, blank=True, null=True, max_length=50)),
                ('smCreatedOn', models.DateTimeField(null=True, auto_now_add=True)),
                ('smModifiedOn', models.DateTimeField(null=True, auto_now=True)),
                ('smUUID', models.UUIDField(editable=False, default=uuid.uuid4)),
                ('smInfo', jsonfield2.fields.JSONField(default={})),
                ('code', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, null=True)),
                ('dbEngine', models.CharField(max_length=20, blank=True, null=True, choices=[('sqlite3', 'sqlLite3'), ('postgres', 'Postgress'), ('mysql', 'mySQL')], default='sqlite3')),
                ('dbName', models.CharField(max_length=200, blank=True, null=True)),
                ('dbUser', models.CharField(max_length=200, blank=True, null=True)),
                ('dbPassword', models.CharField(max_length=200, blank=True, null=True)),
                ('dbHost', models.CharField(max_length=200, blank=True, null=True)),
                ('dbPort', models.CharField(max_length=200, blank=True, null=True)),
                ('smCreatedBy', models.ForeignKey(editable=False, blank=True, null=True, to=settings.AUTH_USER_MODEL, related_name='+')),
                ('smModifiedBy', models.ForeignKey(editable=False, blank=True, null=True, to=settings.AUTH_USER_MODEL, related_name='+')),
                ('smOwningTeam', models.ForeignKey(editable=False, blank=True, null=True, to='protoLib.TeamHierarchy', related_name='+')),
                ('smOwningUser', models.ForeignKey(editable=False, blank=True, null=True, to=settings.AUTH_USER_MODEL, related_name='+')),
            ],
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('smNaturalCode', models.CharField(editable=False, blank=True, null=True, max_length=50)),
                ('smRegStatus', models.CharField(editable=False, blank=True, null=True, max_length=50)),
                ('smWflowStatus', models.CharField(editable=False, blank=True, null=True, max_length=50)),
                ('smCreatedOn', models.DateTimeField(null=True, auto_now_add=True)),
                ('smModifiedOn', models.DateTimeField(null=True, auto_now=True)),
                ('smUUID', models.UUIDField(editable=False, default=uuid.uuid4)),
                ('smInfo', jsonfield2.fields.JSONField(default={})),
                ('code', models.CharField(max_length=200)),
                ('baseType', models.CharField(max_length=50, blank=True, null=True, choices=[('string', 'string'), ('text', 'text'), ('bool', 'bool'), ('int', 'int'), ('sequence', 'sequence'), ('decimal', 'decimal'), ('money', 'money'), ('combo', 'combo'), ('date', 'date'), ('datetime', 'datetime'), ('time', 'time')], default='string')),
                ('prpLength', models.IntegerField(blank=True, null=True)),
                ('prpScale', models.IntegerField(blank=True, null=True)),
                ('prpDefault', models.CharField(max_length=50, blank=True, null=True)),
                ('prpChoices', models.TextField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('isPrimary', models.BooleanField(default=False)),
                ('isLookUpResult', models.BooleanField(default=False)),
                ('isNullable', models.BooleanField(default=False)),
                ('isRequired', models.BooleanField(default=False)),
                ('isReadOnly', models.BooleanField(default=False)),
                ('isForeign', models.BooleanField(editable=False, default=False)),
                ('vType', models.CharField(max_length=50, blank=True, null=True, choices=[('string', 'string'), ('text', 'text'), ('bool', 'bool'), ('int', 'int'), ('sequence', 'sequence'), ('decimal', 'decimal'), ('money', 'money'), ('combo', 'combo'), ('date', 'date'), ('datetime', 'datetime'), ('time', 'time')], default='string')),
                ('isSensitive', models.BooleanField(default=False)),
                ('isEssential', models.BooleanField(default=False)),
                ('crudType', models.CharField(max_length=20, blank=True, null=True, choices=[('editable', 'Default behavior'), ('readOnly', 'Never saved (rules, functions, linked, ...)'), ('insertOnly', 'Never updated (absorbed at the time of the creation field, eg shipping address'), ('updateOnly', 'Adding null or VrDefault, (fixed initial state)'), ('storeOnly', 'Never show on screen (id, json Types, etc)'), ('screenOnly', 'Calculated on the frontend')])),
                ('dbName', models.CharField(max_length=200, blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PropertyEquivalence',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('smNaturalCode', models.CharField(editable=False, blank=True, null=True, max_length=50)),
                ('smRegStatus', models.CharField(editable=False, blank=True, null=True, max_length=50)),
                ('smWflowStatus', models.CharField(editable=False, blank=True, null=True, max_length=50)),
                ('smCreatedOn', models.DateTimeField(null=True, auto_now_add=True)),
                ('smModifiedOn', models.DateTimeField(null=True, auto_now=True)),
                ('smUUID', models.UUIDField(editable=False, default=uuid.uuid4)),
                ('smInfo', jsonfield2.fields.JSONField(default={})),
                ('description', models.TextField(blank=True, null=True)),
                ('smCreatedBy', models.ForeignKey(editable=False, blank=True, null=True, to=settings.AUTH_USER_MODEL, related_name='+')),
                ('smModifiedBy', models.ForeignKey(editable=False, blank=True, null=True, to=settings.AUTH_USER_MODEL, related_name='+')),
                ('smOwningTeam', models.ForeignKey(editable=False, blank=True, null=True, to='protoLib.TeamHierarchy', related_name='+')),
                ('smOwningUser', models.ForeignKey(editable=False, blank=True, null=True, to=settings.AUTH_USER_MODEL, related_name='+')),
            ],
        ),
        migrations.CreateModel(
            name='ProtoTable',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('smNaturalCode', models.CharField(editable=False, blank=True, null=True, max_length=50)),
                ('smRegStatus', models.CharField(editable=False, blank=True, null=True, max_length=50)),
                ('smWflowStatus', models.CharField(editable=False, blank=True, null=True, max_length=50)),
                ('smCreatedOn', models.DateTimeField(null=True, auto_now_add=True)),
                ('smModifiedOn', models.DateTimeField(null=True, auto_now=True)),
                ('smUUID', models.UUIDField(editable=False, default=uuid.uuid4)),
                ('info', jsonfield2.fields.JSONField(default={})),
                ('entity', models.ForeignKey(to='prototype.Entity')),
                ('smCreatedBy', models.ForeignKey(editable=False, blank=True, null=True, to=settings.AUTH_USER_MODEL, related_name='+')),
                ('smModifiedBy', models.ForeignKey(editable=False, blank=True, null=True, to=settings.AUTH_USER_MODEL, related_name='+')),
                ('smOwningTeam', models.ForeignKey(editable=False, blank=True, null=True, to='protoLib.TeamHierarchy', related_name='+')),
                ('smOwningUser', models.ForeignKey(editable=False, blank=True, null=True, to=settings.AUTH_USER_MODEL, related_name='+')),
            ],
            options={
                'permissions': (('list_%(class)', 'Can list available %(class)s'),),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Prototype',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('smNaturalCode', models.CharField(editable=False, blank=True, null=True, max_length=50)),
                ('smRegStatus', models.CharField(editable=False, blank=True, null=True, max_length=50)),
                ('smWflowStatus', models.CharField(editable=False, blank=True, null=True, max_length=50)),
                ('smCreatedOn', models.DateTimeField(null=True, auto_now_add=True)),
                ('smModifiedOn', models.DateTimeField(null=True, auto_now=True)),
                ('smUUID', models.UUIDField(editable=False, default=uuid.uuid4)),
                ('code', models.CharField(editable=False, max_length=200)),
                ('description', models.TextField(blank=True, null=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('metaDefinition', jsonfield2.fields.JSONField(blank=True, null=True)),
                ('entity', models.ForeignKey(to='prototype.Entity', related_name='prototype_set')),
                ('smCreatedBy', models.ForeignKey(editable=False, blank=True, null=True, to=settings.AUTH_USER_MODEL, related_name='+')),
                ('smModifiedBy', models.ForeignKey(editable=False, blank=True, null=True, to=settings.AUTH_USER_MODEL, related_name='+')),
                ('smOwningTeam', models.ForeignKey(editable=False, blank=True, null=True, to='protoLib.TeamHierarchy', related_name='+')),
                ('smOwningUser', models.ForeignKey(editable=False, blank=True, null=True, to=settings.AUTH_USER_MODEL, related_name='+')),
            ],
        ),
        migrations.CreateModel(
            name='ProtoVersionTitle',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('smNaturalCode', models.CharField(editable=False, blank=True, null=True, max_length=50)),
                ('smRegStatus', models.CharField(editable=False, blank=True, null=True, max_length=50)),
                ('smWflowStatus', models.CharField(editable=False, blank=True, null=True, max_length=50)),
                ('smCreatedOn', models.DateTimeField(null=True, auto_now_add=True)),
                ('smModifiedOn', models.DateTimeField(null=True, auto_now=True)),
                ('smUUID', models.UUIDField(editable=False, default=uuid.uuid4)),
                ('versionCode', models.CharField(max_length=50, blank=True, null=True, default='0')),
                ('description', models.TextField(blank=True, verbose_name='Descriptions', null=True)),
                ('active', models.BooleanField(default=True)),
                ('smCreatedBy', models.ForeignKey(editable=False, blank=True, null=True, to=settings.AUTH_USER_MODEL, related_name='+')),
                ('smModifiedBy', models.ForeignKey(editable=False, blank=True, null=True, to=settings.AUTH_USER_MODEL, related_name='+')),
                ('smOwningTeam', models.ForeignKey(editable=False, blank=True, null=True, to='protoLib.TeamHierarchy', related_name='+')),
                ('smOwningUser', models.ForeignKey(editable=False, blank=True, null=True, to=settings.AUTH_USER_MODEL, related_name='+')),
                ('versionBase', models.ForeignKey(blank=True, null=True, to='prototype.ProtoVersionTitle')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Relationship',
            fields=[
                ('property_ptr', models.OneToOneField(primary_key=True, parent_link=True, auto_created=True, serialize=False, to='prototype.Property')),
                ('relatedName', models.CharField(max_length=50, blank=True, null=True)),
                ('baseMin', models.CharField(max_length=50, blank=True, null=True)),
                ('baseMax', models.CharField(max_length=50, blank=True, null=True)),
                ('refMin', models.CharField(max_length=50, blank=True, null=True)),
                ('refMax', models.CharField(max_length=50, blank=True, null=True)),
                ('onRefDelete', models.CharField(max_length=50, blank=True, null=True, choices=[('CASCADE', 'Cascade deletes; the default'), ('PROTECT', 'Prevent deletion of the referenced object by raising ProtectedError, a subclass of django.db.IntegrityError'), ('SET_NULL', 'Set the ForeignKey null; this is only possible if null is True'), ('SET_DEFAULT', 'Set the ForeignKey to its default value; a default for the ForeignKey must be set.  @function si possible'), ('DO_NOTHING', 'Use default Db constraint')])),
                ('typeRelation', models.CharField(max_length=50, blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('prototype.property',),
        ),
        migrations.AddField(
            model_name='prototype',
            name='smVersion',
            field=models.ForeignKey(blank=True, null=True, to='prototype.ProtoVersionTitle', default=1),
        ),
        migrations.AddField(
            model_name='propertyequivalence',
            name='smVersion',
            field=models.ForeignKey(blank=True, null=True, to='prototype.ProtoVersionTitle', default=1),
        ),
        migrations.AddField(
            model_name='propertyequivalence',
            name='sourceProperty',
            field=models.ForeignKey(blank=True, null=True, to='prototype.Property', related_name='sourcePrp'),
        ),
        migrations.AddField(
            model_name='propertyequivalence',
            name='targetProperty',
            field=models.ForeignKey(blank=True, null=True, to='prototype.Property', related_name='targetPrp'),
        ),
        migrations.AddField(
            model_name='property',
            name='entity',
            field=models.ForeignKey(to='prototype.Entity', related_name='property_set'),
        ),
        migrations.AddField(
            model_name='property',
            name='smCreatedBy',
            field=models.ForeignKey(editable=False, blank=True, null=True, to=settings.AUTH_USER_MODEL, related_name='+'),
        ),
        migrations.AddField(
            model_name='property',
            name='smModifiedBy',
            field=models.ForeignKey(editable=False, blank=True, null=True, to=settings.AUTH_USER_MODEL, related_name='+'),
        ),
        migrations.AddField(
            model_name='property',
            name='smOwningTeam',
            field=models.ForeignKey(editable=False, blank=True, null=True, to='protoLib.TeamHierarchy', related_name='+'),
        ),
        migrations.AddField(
            model_name='property',
            name='smOwningUser',
            field=models.ForeignKey(editable=False, blank=True, null=True, to=settings.AUTH_USER_MODEL, related_name='+'),
        ),
        migrations.AddField(
            model_name='property',
            name='smVersion',
            field=models.ForeignKey(blank=True, null=True, to='prototype.ProtoVersionTitle', default=1),
        ),
        migrations.AddField(
            model_name='project',
            name='smVersion',
            field=models.ForeignKey(blank=True, null=True, to='prototype.ProtoVersionTitle', default=1),
        ),
        migrations.AddField(
            model_name='model',
            name='project',
            field=models.ForeignKey(to='prototype.Project'),
        ),
        migrations.AddField(
            model_name='model',
            name='smCreatedBy',
            field=models.ForeignKey(editable=False, blank=True, null=True, to=settings.AUTH_USER_MODEL, related_name='+'),
        ),
        migrations.AddField(
            model_name='model',
            name='smModifiedBy',
            field=models.ForeignKey(editable=False, blank=True, null=True, to=settings.AUTH_USER_MODEL, related_name='+'),
        ),
        migrations.AddField(
            model_name='model',
            name='smOwningTeam',
            field=models.ForeignKey(editable=False, blank=True, null=True, to='protoLib.TeamHierarchy', related_name='+'),
        ),
        migrations.AddField(
            model_name='model',
            name='smOwningUser',
            field=models.ForeignKey(editable=False, blank=True, null=True, to=settings.AUTH_USER_MODEL, related_name='+'),
        ),
        migrations.AddField(
            model_name='model',
            name='smTags',
            field=taggit.managers.TaggableManager(through='taggit.TaggedItem', blank=True, to='taggit.Tag', help_text='A comma-separated list of tags.', verbose_name='Tags'),
        ),
        migrations.AddField(
            model_name='model',
            name='smVersion',
            field=models.ForeignKey(blank=True, null=True, to='prototype.ProtoVersionTitle', default=1),
        ),
        migrations.AddField(
            model_name='entity',
            name='model',
            field=models.ForeignKey(to='prototype.Model', related_name='entity_set'),
        ),
        migrations.AddField(
            model_name='entity',
            name='smCreatedBy',
            field=models.ForeignKey(editable=False, blank=True, null=True, to=settings.AUTH_USER_MODEL, related_name='+'),
        ),
        migrations.AddField(
            model_name='entity',
            name='smModifiedBy',
            field=models.ForeignKey(editable=False, blank=True, null=True, to=settings.AUTH_USER_MODEL, related_name='+'),
        ),
        migrations.AddField(
            model_name='entity',
            name='smOwningTeam',
            field=models.ForeignKey(editable=False, blank=True, null=True, to='protoLib.TeamHierarchy', related_name='+'),
        ),
        migrations.AddField(
            model_name='entity',
            name='smOwningUser',
            field=models.ForeignKey(editable=False, blank=True, null=True, to=settings.AUTH_USER_MODEL, related_name='+'),
        ),
        migrations.AddField(
            model_name='entity',
            name='smVersion',
            field=models.ForeignKey(blank=True, null=True, to='prototype.ProtoVersionTitle', default=1),
        ),
        migrations.AddField(
            model_name='diagramentity',
            name='entity',
            field=models.ForeignKey(to='prototype.Entity'),
        ),
        migrations.AddField(
            model_name='diagramentity',
            name='smCreatedBy',
            field=models.ForeignKey(editable=False, blank=True, null=True, to=settings.AUTH_USER_MODEL, related_name='+'),
        ),
        migrations.AddField(
            model_name='diagramentity',
            name='smModifiedBy',
            field=models.ForeignKey(editable=False, blank=True, null=True, to=settings.AUTH_USER_MODEL, related_name='+'),
        ),
        migrations.AddField(
            model_name='diagramentity',
            name='smOwningTeam',
            field=models.ForeignKey(editable=False, blank=True, null=True, to='protoLib.TeamHierarchy', related_name='+'),
        ),
        migrations.AddField(
            model_name='diagramentity',
            name='smOwningUser',
            field=models.ForeignKey(editable=False, blank=True, null=True, to=settings.AUTH_USER_MODEL, related_name='+'),
        ),
        migrations.AddField(
            model_name='diagramentity',
            name='smVersion',
            field=models.ForeignKey(blank=True, null=True, to='prototype.ProtoVersionTitle', default=1),
        ),
        migrations.AddField(
            model_name='diagram',
            name='project',
            field=models.ForeignKey(to='prototype.Project'),
        ),
        migrations.AddField(
            model_name='diagram',
            name='smCreatedBy',
            field=models.ForeignKey(editable=False, blank=True, null=True, to=settings.AUTH_USER_MODEL, related_name='+'),
        ),
        migrations.AddField(
            model_name='diagram',
            name='smModifiedBy',
            field=models.ForeignKey(editable=False, blank=True, null=True, to=settings.AUTH_USER_MODEL, related_name='+'),
        ),
        migrations.AddField(
            model_name='diagram',
            name='smOwningTeam',
            field=models.ForeignKey(editable=False, blank=True, null=True, to='protoLib.TeamHierarchy', related_name='+'),
        ),
        migrations.AddField(
            model_name='diagram',
            name='smOwningUser',
            field=models.ForeignKey(editable=False, blank=True, null=True, to=settings.AUTH_USER_MODEL, related_name='+'),
        ),
        migrations.AddField(
            model_name='diagram',
            name='smVersion',
            field=models.ForeignKey(blank=True, null=True, to='prototype.ProtoVersionTitle', default=1),
        ),
        migrations.AddField(
            model_name='relationship',
            name='refEntity',
            field=models.ForeignKey(null=True, to='prototype.Entity', related_name='refEntity_set'),
        ),
        migrations.AlterUniqueTogether(
            name='prototype',
            unique_together=set([('entity', 'code', 'smOwningTeam')]),
        ),
        migrations.AlterUniqueTogether(
            name='propertyequivalence',
            unique_together=set([('sourceProperty', 'targetProperty', 'smOwningTeam')]),
        ),
        migrations.AlterUniqueTogether(
            name='property',
            unique_together=set([('entity', 'code', 'smOwningTeam')]),
        ),
        migrations.AlterUniqueTogether(
            name='project',
            unique_together=set([('code', 'smOwningTeam')]),
        ),
        migrations.AlterUniqueTogether(
            name='model',
            unique_together=set([('project', 'code', 'smOwningTeam')]),
        ),
        migrations.AlterUniqueTogether(
            name='entity',
            unique_together=set([('model', 'code', 'smOwningTeam')]),
        ),
        migrations.AlterUniqueTogether(
            name='diagramentity',
            unique_together=set([('diagram', 'entity', 'smOwningTeam')]),
        ),
        migrations.AlterUniqueTogether(
            name='diagram',
            unique_together=set([('project', 'code', 'smOwningTeam')]),
        ),
    ]
