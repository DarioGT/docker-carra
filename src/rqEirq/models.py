# -*- coding: utf-8 -*-

from django.db import models
from protoExt.utils.utilsConvert import slugify2
from protoLib.models.protomodel import ProtoModelBase



TYPESOURCE_CHOICES = (
        ('INTERNE', 'Int'),
        ('EXTERNE', 'Ext'),
        ('ACHAT', 'Achat'),
        ('FEDERAL', 'Fédéral'),
        ('PRODUIT', 'Produit'),
        ('REF', 'Référentiel'),
    )



class Responsable(ProtoModelBase):
    code  = models.CharField(blank=True, null=True, max_length=200)
    label  = models.CharField(blank=True, null=True, max_length=200)
    coordonnees  = models.CharField(blank=True, null=True, max_length=200)
    notes   = models.CharField(blank=True, null=True, max_length=200)

    def __str__(self):
        return slugify2(self.code )

    unicode_sort = ('code',)



class Source(ProtoModelBase):
    code  = models.CharField(blank=True, null=True, max_length=200)
    label  = models.CharField(blank=True, null=True, max_length=200)
    typeSource = models.CharField( blank= True, null= True, max_length=20, choices=TYPESOURCE_CHOICES )
    responsable = models.ForeignKey('Responsable', blank= True, null= True)

    def __str__(self):
        return slugify2(self.code )

    unicode_sort = ('code',)

    protoExt = {
        "gridConfig": {
            "listDisplay": ["__str__", "typeSource", "responsable"]
        },
        "actions": [
            {"name": "doGraphMerveille", "selectionMode": "multiple"},
        ],
    }


class Fichier(ProtoModelBase):
    code  = models.CharField(blank=True, null=True, max_length=200)
    label  = models.CharField(blank=True, null=True, max_length=200)
    source = models.ForeignKey('Source', blank= True, null= True)
    responsable = models.ForeignKey('Responsable', blank= True, null= True)

    def __str__(self):
        return slugify2(self.code )

    unicode_sort = ('code',)


class Dependance(ProtoModelBase):
    produit = models.ForeignKey('Source', blank= True, null= True)
    fichier = models.ForeignKey('Fichier', blank= True, null= True)

    def __str__(self):
        return slugify2(self.produit.code + '_' + self.fichier.code )

