# -*- coding: utf-8 -*-

from django.db import models
from protoExt.utils.utilsConvert import slugify2
from protoLib.models.protomodel import ProtoModelBase



# TYPERESPONSABLE_CHOICES = (
#         ('Persona', 'Per'),
#         ('UniteOrg', 'UO'),
#     )


class Resource(ProtoModelBase):
    #  M. Xxxx,  BussUnit 
    code  = models.CharField(blank=True, null=True, max_length=200)

    # Hierarchy
    #parent = models.ForeignKey(self, blank= True, null= True)

    # Nom, Prenom ;  BUnit ; CCost  
    description  = models.CharField(blank=True, null=True, max_length=200)

    # Personne, BussUnit 
    typeResource = models.CharField( blank= True, null= True, max_length=20 )

    # Analiste, Technique, Architect 
    catResource = models.CharField( blank= True, null= True, max_length=20 )

    email  = models.CharField(blank=True, null=True, max_length=200)
    coordonnees  = models.CharField(blank=True, null=True, max_length=200)
    notes   = models.CharField(blank=True, null=True, max_length=200)

    # Sum of ResourceSkill.Capacity  ( in hours, ) 
    capacityResource  = models.IntegerField(blank=True, null=True)

    # Sum of ResourceSkill.CapacityAssigned
    capacityAssigned  = models.IntegerField(blank=True, null=True)

    # Sum of ResourceSkill.CapacityAssigned
    capacityIdle  = models.IntegerField(blank=True, null=True)


    def __str__(self):
        return slugify2(self.code )

    unicode_sort = ('code',)



class Skill(ProtoModelBase):
    # SQL, SAS, LEAN
    code  = models.CharField(blank=True, null=True, max_length=200)
    label  = models.CharField(blank=True, null=True, max_length=200)
    description = models.CharField(blank=True, null=True, max_length=500)

    # Tech, Methode, Leader 
    skillType = models.CharField( blank= True, null= True, max_length=20)


    # Sum of TaskSkill Capacity needed ( hours, ) 
    capacityNeed  = models.IntegerField(blank=True, null=True)

    # Sum of TaskSkill CapacityAssigned by Task
    capacityAssigned  = models.IntegerField(blank=True, null=True)

    # Sum of TaskSkill CapacityIdle
    capacityAvailable  = models.IntegerField(blank=True, null=True)

    # capacityNeed - capacityAssigned
    capacityGap  = models.IntegerField(blank=True, null=True)


    def __str__(self):
        return slugify2(self.code )


class ResourceSkill(ProtoModelBase):
    resource = models.ForeignKey(Resource, blank= True, null= True)
    skill = models.ForeignKey(Skill, blank= True, null= True)

    # Interet, Competent, Expert 
    skillLevel  = models.CharField(blank=True, null=True, max_length=200)

    # Capacity in ( hours, ) 
    capacityResource  = models.IntegerField(blank=True, null=True)

    # Sum of CapacityAssigned
    capacityAssigned  = models.IntegerField(blank=True, null=True)

    # Sum of CapacityAssigned
    capacityIdle  = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return slugify2(self.skill.code + '_' + self.resource.code )



#  ----------------------------------------------------------------


class Task(ProtoModelBase):
    #  organizational need 
    code  = models.CharField(blank=True, null=True, max_length=200)
    label  = models.CharField(blank=True, null=True, max_length=200)
    description = models.CharField(blank=True, null=True, max_length=500)

    notes = models.CharField(blank=True, null=True, max_length=500)
    urlDoc = models.CharField(blank=True, null=True, max_length=500)

    typeTask = models.CharField( blank= True, null= True, max_length=20 )

    # PO : product owner
    resource = models.ForeignKey(Resource, blank= True, null= True, related_name='reposable_set')


    # Sum of ResourceSkill.Capacity  ( in hours, ) 
    capacityResource  = models.IntegerField(blank=True, null=True)

    # Sum of ResourceSkill.CapacityAssigned
    capacityAssigned  = models.IntegerField(blank=True, null=True)

    # Sum of ResourceSkill.CapacityAssigned
    capacityIdle  = models.IntegerField(blank=True, null=True)


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


class TaskSkill(ProtoModelBase):
    # skill need
    task = models.ForeignKey(Task, blank= True, null= True)
    skill = models.ForeignKey(Skill, blank= True, null= True)


    # Competent, Expert 
    skillLevel  = models.CharField(blank=True, null=True, max_length=200)

    # Total Capacity needed ( hours, ) 
    capacityNeed  = models.IntegerField(blank=True, null=True)

    # Sum of CapacityAssigned by Task
    capacityAssigned  = models.IntegerField(blank=True, null=True)

    # Sum of CapacityIdle
    capacityAvailable  = models.IntegerField(blank=True, null=True)

    # capacityNeed - capacityAssigned
    capacityGap  = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return slugify2(self.task.code + '_' + self.skill.code )


# ---------------------------------------------------


class CapacityAssigned(ProtoModelBase):
    # skill need vs skill Capacity
    taskSkill = models.ForeignKey(TaskSkill, blank= True, null= True)
    resourceSkill = models.ForeignKey(ResourceSkill, blank= True, null= True)

    # Total Capacity assigned ( hours, ) 
    capacityAssigned  = models.IntegerField(blank=True, null=True)


    def __str__(self):
        return slugify2(self.taskSkill + '_' + self.resourceSkill.code )



# ---------------------------------------------


class SkillResSupport(ProtoModelBase):
    code  = models.CharField(blank=True, null=True, max_length=200)

    # Certification, Experience. Etudes
    resourceSkill = models.ForeignKey(ResourceSkill, blank= True, null= True)

    # Cerfication, DEC, BAC, Mandates ( Experience )
    skillSupType = models.CharField( blank= True, null= True, max_length=50)
 
    # accredited experience detail ( temp mandate )
    skillSupDetail = models.CharField( blank= True, null= True, max_length=50)
    notes = models.CharField(blank=True, null=True, max_length=500)

    def __str__(self):
        return slugify2(self.code )

