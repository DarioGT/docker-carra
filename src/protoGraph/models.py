# -*- coding: utf-8 -*-

from django.db import models
from protoExt.utils.utilsConvert import slugify2
from protoLib.models.protomodel import ProtoModelBase, ProtoModelExt 


class NodeCategory(ProtoModelExt):
    code  = models.CharField(blank=True, null=True, max_length=200)
    description  = models.CharField(blank=True, null=True, max_length=200)

    def __str__(self):
        return slugify2(self.code )

    unicode_sort = ('code',)

class EdgeCategory(ProtoModelExt):
    code  = models.CharField(blank=True, null=True, max_length=200)
    description  = models.CharField(blank=True, null=True, max_length=200)

    def __str__(self):
        return slugify2(self.code )

    unicode_sort = ('code',)


class Node(ProtoModelExt):
    code  = models.CharField(blank=True, null=True, max_length=200)
    category = models.ForeignKey( NodeCategory, blank= True, null= True)

    label  = models.CharField(blank=True, null=True, max_length=200)
    description  = models.CharField(blank=True, null=True, max_length=200)

    idSource  = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return slugify2(self.code )

    unicode_sort = ('code',)

    class Meta:
        unique_together = ('idSource', 'category')


class Edge(ProtoModelExt):
    code  = models.CharField(blank=True, null=True, max_length=200)
    node0 = models.ForeignKey( Node, blank= True, null= True, related_name='node0_set')
    node1 = models.ForeignKey( Node, blank= True, null= True, related_name='node1_set')

    label  = models.CharField(blank=True, null=True, max_length=200)
    category = models.ForeignKey( EdgeCategory, blank= True, null= True)
    description  = models.CharField(blank=True, null=True, max_length=200)

    class Meta:
        unique_together = ('node0', 'node1')

    protoExt = {
        "gridConfig": {
            "listDisplay": ["code", "node0", "node1"]
        },
        "actions": [
            {"name": "doGeneraBasicNet"},
        ],
    }


class Canvas(ProtoModelBase):
    code  = models.CharField(blank=True, null=True, max_length=200)
    description  = models.CharField(blank=True, null=True, max_length=200)

    def __str__(self):
        return slugify2(self.code )

    unicode_sort = ('code',)

class CanvasDetail(ProtoModelBase):
    canvas = models.ForeignKey( Canvas, blank= True, null= True)
    edge = models.ForeignKey( Edge, blank= True, null= True)

    def __str__(self):
        return slugify2(self.canvas.code + '_' + self.edge.code )

