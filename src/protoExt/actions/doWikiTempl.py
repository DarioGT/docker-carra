# -*- coding: utf-8 -*-


  
from protoExt.utils.utilsConvert import slugify2




def doWikiTemplate(request, queryset, parameters):


    # Loop 
    for dView in queryset:

        protoMeta = doWikiFile( dView.metaDefinition ) 
        



def doWikiFile( protoMeta ):


    # 

    lFields = []
    lZooms =  []

    viewEntity = protoMeta['viewEntity']
    lApp, lEntity =  viewEntity.lower().split('.')


    for lField in protoMeta['fields']:
        fName = lField['name']
        if isAdmField( fName ): continue

        myZoomModel = lField.get('zoomModel', '')
        if (len(myZoomModel) > 0) :
            zooms.append(  lField )
        else: 
            fields.append(  lField )


    sAux  = "{% load prototags %}\n"
    sAux += "{% block content %}\n\n"

    sAux += "======= {0} : {{ {1}.__str__ |capfirst }} =======\n\n".format( protoMeta['shortTitle'], lEntity )
    sAux += "^Property ^Value ^\n"

    for lField in lFields:

        sAux += "|{0} |{{ {1}.{2} }}|\n".format( lField['header'], lEntity, lField['name'] )

    sAux += "====== References ======\n\n"
    sAux += "^Property ^Value ^\n"

    for lField in lZooms:

        sAux += "|{0} |{{ {1}.{2}.wkFullPageName }}|\n".format( lField['header'], lEntity, lField['name'] )


    for lDet in protoMeta['detailsConfig']:
        lDetName = lDet['conceptDetail'].split('.')[1] 

        sAux += "====== {0} ======\n".format( lDet['menuText'] )
        sAux += "^{0}^\n".format()
        sAux += "{% for entity in project.model_set.all %}|{{ entity.wkFullPageName }}|{{ entity.description|default:\".. description\" }} |\n"
        sAux += "{% endfor %}\n"

    sAux += "{% endblock %}"


    return sAux  



    for lField in cBase.protoMeta['fields']:
        fName = lField['name']
        myZoomModel = lField.get('zoomModel', '')
        if (len(myZoomModel) > 0) and (myZoomModel != cBase.protoMeta['viewEntity']):
            relModels[fName] = {
                'zoomModel': myZoomModel, 'fkId': lField.get('fkId', ''), 'loaded': False}

    # Verifica si existen reemplazos por hacer ( cpFromField )
    # 1.  Marca los zooms q estan referenciados
    bCopyFromFld = False
    for lField in cBase.protoMeta['fields']:
        fName = lField['name']
        if (lField.get('cpFromField') is None or lField.get('cpFromZoom') is None):
            continue

        bCopyFromFld = True
        lField['isAbsorbed'] = True

        # Marca el zoom
        try:
            relModel = relModels[lField.get('cpFromZoom')]
            relModel['loaded'] = True
        except:
            pass

