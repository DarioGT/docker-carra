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
    description = models.CharField(blank=True, null=True, max_length=500)
    notes = models.CharField(blank=True, null=True, max_length=500)
    urlDoc = models.CharField(blank=True, null=True, max_length=500)

    typeSource = models.CharField( blank= True, null= True, max_length=20, choices=TYPESOURCE_CHOICES )

    responsable = models.ForeignKey('Responsable', blank= True, null= True, related_name='responsable_set')
    pilote = models.ForeignKey('Responsable', blank= True, null= True, related_name='pilote_set')

    def __str__(self):
        return slugify2(self.code )

    unicode_sort = ('code',)

    protoExt = {
        "gridConfig": {
            "listDisplay": ["__str__", "typeSource", "responsable"]
        },
        "actions": [
            {"name": "doGraphMerveille", "selectionMode": "multiple", 
              "actionParams": [
                {"name" : "NewGraph", "type" : "boolean", "tooltip" : "Clear old graph" }
                ], 
            },
        ],
    }

class Technologie(ProtoModelBase):
    code  = models.CharField(blank=True, null=True, max_length=200)
    label  = models.CharField(blank=True, null=True, max_length=200)
    description = models.CharField(blank=True, null=True, max_length=500)

    typeT = models.CharField( blank= True, null= True, max_length=20)

    def __str__(self):
        return slugify2(self.code )


class Fichier(ProtoModelBase):
    code  = models.CharField(blank=True, null=True, max_length=200)
    label  = models.CharField(blank=True, null=True, max_length=200)
    typeF  = models.CharField(blank=True, null=True, max_length=50)

    emplacement = models.CharField(blank=True, null=True, max_length=50)
    frequence = models.CharField(blank=True, null=True, max_length=50)
    reception = models.CharField(blank=True, null=True, max_length=50)
    scenario = models.CharField(blank=True, null=True, max_length=50)

    codeUntTraitement = models.CharField(blank=True, null=True, max_length=50)
    chaineExtraction = models.CharField(blank=True, null=True, max_length=50)
    chaineNettoyage = models.CharField(blank=True, null=True, max_length=50)
    chaineChargement = models.CharField(blank=True, null=True, max_length=50)

    typeExploitation = models.CharField(blank=True, null=True, max_length=50)
    dgu = models.CharField(blank=True, null=True, max_length=50)
    vpa = models.IntegerField(blank=True, null=True)

    urlDoc = models.CharField(blank=True, null=True, max_length=500)
    urlModel = models.CharField(blank=True, null=True, max_length=500)
    urlMeta = models.CharField(blank=True, null=True, max_length=500)


    source = models.ForeignKey('Source', blank= True, null= True)
    responsable = models.ForeignKey('Responsable', blank= True, null= True)

    description = models.CharField(blank=True, null=True, max_length=500)
    notes = models.CharField(blank=True, null=True, max_length=500)

    def __str__(self):
        return slugify2(self.code )

    unicode_sort = ('code',)


class TechChargement(ProtoModelBase):
    fichier = models.ForeignKey('Fichier', blank= True, null= True)
    technologie = models.ForeignKey('Technologie', blank= True, null= True)

    def __str__(self):
        return slugify2(self.fichier.code + '_' + self.ressource.code )


class RessourceTech(ProtoModelBase):
    ressource = models.ForeignKey('Responsable', blank= True, null= True)
    technologie = models.ForeignKey('Technologie', blank= True, null= True)

    def __str__(self):
        return slugify2(self.fichier.code + '_' + self.ressource.code )



class Dependance(ProtoModelBase):
    produit = models.ForeignKey('Source', blank= True, null= True)
    fichier = models.ForeignKey('Fichier', blank= True, null= True)

    def __str__(self):
        return slugify2(self.produit.code + '_' + self.fichier.code )

