# -*- coding: utf-8 -*-

from django.db import models
from jsonfield2 import JSONField
from .usermodel import AUTH_USER_MODEL

from protoLib.models import TeamHierarchy 
from protoLib.middleware import CurrentUserMiddleware
from protoLib.getStuff import getUserTeam

from .protomanager import TeamPermissionManager, ProtoJSONManager

import uuid 
from protoExt.utils.utilsFile import joinPath
from protoExt.utils.utilsConvert import slugify2


smControlFields = [
    'smOwningUser', 'smOwningTeam', 'smOwningUser_id', 'smOwningTeam_id', \
    'smCreatedBy',  'smModifiedBy', 'smCreatedBy_id',  'smModifiedBy_id', \
    'smCreatedOn', 'smModifiedOn', \
    'smWflowStatus', 'smRegStatus', \
    'smNaturalCode', 'smUUID', 'smVersion', 'smVersion_id' ]


class ProtoModelBase(models.Model):
    """
    model for user entities creation     ( sm  security mark )
    related_name="%(app_label)s_%(class)s"
    """ 

    smNaturalCode = models.CharField(max_length=50, null=True, blank=True, editable=False)
    smRegStatus = models.CharField(max_length=50, null=True, blank=True, editable=False)
    smWflowStatus = models.CharField(max_length=50, null=True, blank=True, editable=False)

    smOwningUser = models.ForeignKey(AUTH_USER_MODEL, null=True, blank=True, related_name='+', editable=False)
    smOwningTeam = models.ForeignKey(TeamHierarchy, null=True, blank=True, related_name='+', editable=False)

    smCreatedBy = models.ForeignKey(AUTH_USER_MODEL, null=True, blank=True, related_name='+', editable=False)
    smModifiedBy = models.ForeignKey(AUTH_USER_MODEL, null=True, blank=True, related_name='+', editable=False)

    smCreatedOn = models.DateTimeField( auto_now_add =True, editable=False, null=True, blank=True )
    smModifiedOn = models.DateTimeField( auto_now =True, editable=False, null=True, blank=True)

    smUUID = models.UUIDField( default=uuid.uuid4, editable=False)

    # Si la tabla no es manajada por teams,  debe cambiarse el manager 
    objects = TeamPermissionManager()
    smObjects = models.Manager()    

    # Security indicator used by control permissions
    _protoObj = True
    
    # En los modelos q esto es falso NaturalCode debe manejarse directamente      
    _setNaturalCode = True

    class Meta:
        abstract = True

        # https://docs.djangoproject.com/en/1.8/ref/models/options/#permissions
        permissions = (
            ("list_%(class)", "Can list available %(class)s"),
        )
        
    def save(self, *args, **kwargs):
        # Disabled for loaddata
        isRaw = kwargs.get('raw', False)

        if not isRaw :
            cuser = CurrentUserMiddleware.get_user( False )

            # Set fix version 180131 
            self.smVersion_id = 1 
            
            if self._setNaturalCode:
                self.smNaturalCode = self.__str__()
                 
            if cuser: 
                setattr(self, 'smModifiedBy', cuser)
    
                # Insert 
                if not self.pk:   
                    setattr(self, 'smCreatedBy', cuser)
                    setattr(self, 'smOwningUser', cuser)
                    setattr(self, 'smOwningTeam', getUserTeam( cuser))
        
        super(ProtoModelBase, self).save(*args, **kwargs)


    @property
    def wkFilePath(self):
        #  app/model 
        return  joinPath( self._meta.app_label , self._meta.verbose_name.title() ).lower() 


    @property
    def wkPage(self):
        # str-id  (  code-0001  )
        sAux = self.__str__()
        if len( sAux ) > 16: sAux = sAux[:16]  
        
        return slugify2( self.__str__()  + '-{:08d}'.format( self.id ) ) 



    @property
    def wkFullPageName(self):
        #  :app:model:page | __str__
        sAux = joinPath( self.wkFilePath , self.wkPage ) 
        sAux = '[[:' + sAux.replace('/', ':').replace('\\', ':') + '|' + self.__str__() + ']]'
        return  sAux 



class ProtoModelExt(ProtoModelBase):
    """
    Tabla modelo para la creacion de entidades de usuario  ( sm  security mark )
    with json fields  ( UDPs ) and filtering allow 
    """ 

    smInfo = JSONField(default={})

    objects = ProtoJSONManager(json_fields = ['smInfo'])
    smObjects = models.Manager()

    _protoJson = True

    class Meta:
        abstract = True




def setSecurityInfo(dEntity, data, user_profile, ins):
    pass
        