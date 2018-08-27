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


# 	Sheet et list selection
    cRep = cAux()
    cRep.sheetName = request.POST.get('sheetName', '' )
    _getSheetConf( cBase, cRep  )

    try:
        # Obtiene las filas del cBase.modelo
        Qs = getQSet(cBase)

    except Exception as e:
        traceError()
        message = getReadableError(e)
        return JsonError(message)

    cRep.wikiPath = getParameter('wikiPath', '/var/www/dokuwiki/data/pages')

    for reg in Qs:
        try:
            msgError = _doWikiFile(cBase, cRep , reg)
            if msgError: return msgError 

        except Exception as e:
            traceError()
            message = getReadableError(e)
            return JsonError(message)

    return JsonSuccess()

    

def _doWikiFile(cBase, cRep,  reg ):
    """
    nameSpace     App.Model 
    pageExpr      prefix, Field
    """
 
    myPath  = joinPath( cRep.wikiPath, reg.wkFilePath ) 

    # Verify path              
    filePath = verifyDirPath( myPath )
    if not filePath: return JsonError('invalid path : %s' % myPath )
    filePath = joinPath( filePath , reg.wkPage ) + '.txt'


    # Carga el template   
    t = loader.get_template( cRep.template )
    wFile = t.render(Context({ 
          cRep.regName : reg, 
          }))

    WriteFile(filePath, wFile, 'w')



def _getSheetConf(cBase, cRep):
    """ 
    Obtiene un sheetConfig dado su nombre
    recibe  la definicion ( protoMeta ) y el nombre ( str )
    retorna sheetConfig ( obj )
    """

    sheetConfs = cBase.protoMeta.get('sheetConfig', [])

    # Los recorre todos pero se queda con el primero en caso de no encotrarl el nombre seleccionado
    cRep.sheetConf = None
    for item in sheetConfs:
        if cRep.sheetConf == None:
            cRep.sheetConf = item
        if item.get('name', '') == cRep.sheetName :
            cRep.sheetConf = item
            break

    if cRep.sheetConf == None:
        return "sheet definition not found %s" % cRep.sheetName  

    cRep.nSpaceExpr = cRep.sheetConf.get( 'nameSpace', '' )
    cRep.pageExpr = cRep.sheetConf.get( 'pageExpr', '' )
    cRep.template = cRep.sheetConf.get( 'template', '' )
    cRep.regName = slugify2( cBase.viewCode.split('.')[1] )  
    

