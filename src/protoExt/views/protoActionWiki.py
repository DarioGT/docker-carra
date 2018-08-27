# -*- coding: utf-8 -*-

# Manejo de reportes basdaos en plantillas ( sheets )
#Dg 121105   --------------------------------------------------
#
from .protoActionList  import getQSet
from protoExt.utils.utilsBase import  getReadableError
from protoExt.utils.utilsWeb import JsonError, JsonSuccess

from protoExt.views.protoActionList import prepareListEnv
from protoExt.utils.utilsBase import traceError
from django.template import loader
from django.template.context import Context
from protoExt.views.getStuff import getParameter
from protoExt.utils.utilsFile import joinPath, verifyDirPath, WriteFile
from protoLib.getStuff import cAux
from protoExt.utils.utilsConvert import slugify2


def doExportWiki( modeladmin, request, queryset, parameters):


#   El QSet viene con la lista de Ids  
    if queryset.count() != 1:
        return  {'success':False, 'message' : 'No record selected' }

    try: 
        pass
#        Do no delete 
#        from multiprocessing import Process
#        p = Process (target= getDbSchemaDef ,args=( queryset[0] , request ))
#        p.start()
    
#   Recorre los registros selccionados   
    except:
        traceError()
        return  {'success':False, 'message' : 'Load error' }
        pass
        
    return {'success':True, 'message' :  'runing ...' } 




def protoWiki(request):
    """ 
    exportWiki  

    input:  opcion, template,  Qs ( list of  ids )

    ES: La plantilla de base sera solicitada al usuario, si se deja en blanco usara el sheetSelector o el default
        Los detalles no tienen selector, siempre se usara el template marcado en el detalle.
    """

    try:
        cBase, message = prepareListEnv(request)
        if message: return message

    except Exception as e:
        traceError()
        message = getReadableError(e)
        return JsonError(message)


    # Obtiene las filas del cBase.modelo
    try:
        Qs = getQSet(cBase)

    except Exception as e:
        traceError()
        message = getReadableError(e)
        return JsonError(message)

    cBase.wikiPath = getParameter('wikiPath', '/var/www/dokuwiki/data/pages')

    for reg in Qs:
        try:
            msgError = _doWikiFile(cBase, reg)
            if msgError: return msgError 

        except Exception as e:
            traceError()
            message = getReadableError(e)
            return JsonError(message)

    return JsonSuccess()

    cBase.viewEntity.lower().split('.') 

def _doWikiFile(cBase,  reg ):
    """
    nameSpace     App.Model 
    pageExpr      prefix, Field
    """
 
    myPath  = joinPath( cBase.wikiPath, reg.wkFilePath ) 
    regName = slugify2( cBase.viewCode.split('.')[1] )

    # Verify path              
    filePath = verifyDirPath( myPath )
    if not filePath: return JsonError('invalid path : %s' % myPath )
    filePath = joinPath( filePath , reg.wkPage ) + '.txt'

    # Templatefile
    lApp, lEntity =  cBase.viewEntity.lower().split('.') 
    template = '{0}/wiki{1}.txt'.format( lApp, lEntity )

    # Carga el template   
    t = loader.get_template( template )
    wFile = t.render(Context({regName : reg, }))

    WriteFile(filePath, wFile, 'w')



