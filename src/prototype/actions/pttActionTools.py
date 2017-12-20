'''
Created on 2013-12-21

@author: dario
'''

from protoExt.utils.utilsConvert import slugify2 

TypeEquivalence = { 
        'bool'      :   'BooleanField',
        'string'    :   'CharField', 
        'date'      :   'DateField', 
        'datetime'  :   'DateTimeField', 
        'decimal'   :   'DecimalField',
        'float'     :   'FloatField',
        'int'       :   'IntegerField',
        'text'      :   'TextField',
        'time'      :   'TimeField',
        'jsonfield' :   'JSONField',
    }



def getViewCode( pEntity, viewSufx = '' ):
    # Allow sufix for create +1 view / entity
    if len( viewSufx ) > 0: viewSufx = '-' + viewSufx
    return slugify2( pEntity.model.code + '-' + pEntity.code ) + viewSufx

