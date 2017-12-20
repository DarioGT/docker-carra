'''
Created on Feb 1, 2016

@author: dario
'''


from django.db import models
from django.contrib.contenttypes.models import ContentType
from protoLib.models.protomodel import ProtoModelBase


class VersionTitle(ProtoModelBase):
    """
    Deprecated 17/12  Dgt 
    """
    versionCode = models.CharField(max_length=50, null=True, blank=True, editable=True, default='0')
    versionBase = models.ForeignKey('self', null=True, blank=True, )

    description = models.TextField( verbose_name=u'Descriptions', blank=True, null=True)
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True

    def __str__(self):
        return "%s" % (self.versionCode)

    protoExt = {
        "gridConfig": {
            "listDisplay": ["__str__", "description", "smCreatedBy"]
        }, 
        "actions": [
            { "name": "doCopyVersion", "selectionMode" : "single"}, 
            { "name": "doDeleteVersion", "selectionMode" : "single"}, 
        ],
                
    }




class ProtoVersionTitle(VersionTitle):

    # deprecated :: from prototype/models.py  
    # doVersion.py 

    versionHeaders = [
        "prototype.project",
        "prototype.model",
        "prototype.entity",
        "prototype.property",
        "prototype.propertyequivalence",
        "prototype.diagram",
        "prototype.diagramentity",
        "prototype.prototype",
    ]

    versionExclude = [
        "prototype.relationship" ,
        "prototype.prototable",
    ]

    protoExt = {
        "gridConfig": {
            "listDisplay": ["__str__", "description", "smCreatedBy"]
        }, 
        "actions": [
            { "name": "doCopyVersion", "selectionMode" : "single"}, 
            { "name": "doDeleteVersion", "selectionMode" : "single"}, 
        ],
        "contextTo": [{
            "deftModel": "prototype.project",
            "deftField": "smVersion_id",
        }, {
            "deftModel": "prototype.model",
            "deftField": "smVersion_id",
        }, {
            "deftModel": "prototype.entity",
            "deftField": "smVersion_id",
        }, {
            "deftModel": "prototype.property",
            "deftField": "smVersion_id",
        }, {
            "deftModel": "prototype.propertyequivalence",
            "deftField": "smVersion_id",
        }, {
            "deftModel": "prototype.diagram",
            "deftField": "smVersion_id",
        }, {
            "deftModel": "prototype.diagramentity",
            "deftField": "smVersion_id",
        }, {
            "deftModel": "prototype.prototype",
            "deftField": "smVersion_id",
        }],
    }

