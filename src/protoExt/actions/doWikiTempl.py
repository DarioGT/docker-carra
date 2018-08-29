# -*- coding: utf-8 -*-

from datetime import datetime  
from protoExt.utils.utilsConvert import slugify2
from protoExt.views.protoField import isAdmField
import os
from protoExt.utils.utilsFile import verifyDirPath


def doWikiTemplate(request, queryset, parameters):


    # Loop 
    for dView in queryset:

        doWikiFile( dView.metaDefinition ) 



def doWikiFile( protoMeta ):
    # Prepare DokuWiki default template  

    lFields = []
    lZooms =  []

    lApp, lEntity =  protoMeta['viewEntity'].split('.')
    lEntity = lEntity.lower()


    for lField in protoMeta['fields']:
        if isAdmField( lField['name'] ): continue
        if lField['type'] == 'foreignid': continue

        if lField['type'] == 'foreigntext' :
            lZooms.append(  lField )
        else: 
            lFields.append(  lField )


    sAux  = "{% load prototags %}{% block content %}\n"

    sAux += "======= {0} : $a {1} |capfirst $b =======\n\n".format( protoMeta['shortTitle'], lEntity )
    sAux += "^Property ^Value ^\n"

    for lField in lFields:
        fName = lField['name']
        lHeader = lField.get( 'header', fName ) 
        if  fName == '__str__' : 
            fName = lEntity
        else: 
            fName = lEntity + '.' + fName

        sAux += "|{0} |$a {1} $b|\n".format( lHeader, fName )


    sAux += "\n====== References ======\n"
    sAux += "^Zooms ^Value^ \n"

    for lField in lZooms:
        fName = lField['name']
        lHeader = lField.get( 'header', fName ) 
        sAux += "|{0} |$a {1}.{2}.wkFullPageName $b|\n".format( lHeader , lEntity, fName )


    sAux += "\n====== Details ======\n\n"


    for lDet in protoMeta['detailsConfig']:

        lDetName = lDet['detailName'].split('.')[1].lower()

        sAux += "^{0}^\n".format( lDet['menuText'] )
        sAux += "{% " + "for det in {0}.{1}_set.all".format( lEntity, lDetName ) + " %}" 
        sAux += "|$a det.wkFullPageName $b|\n"
        sAux += "{% endfor %}\n\n"

    sAux += "{% endblock %}"
    sAux += "//AutoTemplate :{0}//".format( datetime.now() ) 

    sAux = sAux.replace( '$a', '{{').replace('$b', '}}')


    # File 
    from django.conf import settings

    PPATH = os.path.join(  settings.BASE_DIR, lApp, 'templates', 'wiki' ) 
    filePath = verifyDirPath( PPATH )
    if not filePath: 
        # rise error NoPATH 
        return False
    

    fileName = os.path.join( filePath,  lApp + '.' + lEntity + '.dkwk' )
    fo = open( fileName , "wb")
    fo.write( sAux.encode('utf-8'))
    fo.close()
 
 