# -*- coding: utf-8 -*-

from protoExt.utils.utilsBase import getReadableError, traceError
from protoExt.actions.doWikiTempl import doWikiTemplate


def doSetContext(modeladmin, request, queryset, parameters):
    """ 
    find and replace sobre la tabla actual 
    parameters   campo,  findText, replaceText 
    """

#   El QSet viene con la lista de Ids
    if queryset.count() > 1:
        return  {'success':False, 'message' : 'Single or null selection required'}


    from protoExt.actions.setContext import actionSetContext

    try:
        result = actionSetContext(request, queryset, parameters)

    except Exception as e:
        traceError()
        result = {'success':False, 'message' : getReadableError(e) }

    return result


def doAddUser(modeladmin, request, queryset, parameters):
    """ 
    Add user  
    parameters : sUser,sPwd,sMail,sTeam,[sGroups]
    """

#   El QSet viene con la lista de Ids
    from protoExt.actions.addUser import actionAddUser

    try:
        result = actionAddUser(request, queryset, parameters)

    except Exception as e:
        traceError()
        result = {'success':False, 'message' : getReadableError(e) }

    return result


def doAddUsers(modeladmin, request, queryset, parameters):
    """ 
    Add users  
    parameters : sUser,sPwd,sMail,sTeam,Group1, .., Group(n) \n
    """

#   El QSet viene con la lista de Ids
    from protoExt.actions.addUser import actionAddUsers

    try:
        result = actionAddUsers(request, queryset, parameters)

    except Exception as e:
        traceError()
        result = {'success':False, 'message' : getReadableError(e) }

    return result



def doFindReplace(modeladmin, request, queryset, parameters):
    """ 
    generique find and replace 
    parameters   field,  findText, replaceText 
    """

#   QSet User selection registers ( Ids ) 
    if queryset.count() < 1:
        return  {'success':False, 'message' : 'Multiple selection required'}

    if len(parameters) != 3:
        return  {'success':False, 'message' : 'required: fieldName, findText, replaceText' }

    from protoLib.actions.findReplace import actionFindReplace
    return actionFindReplace(request, queryset, parameters)





def doGeneraWikiTemplate(modeladmin, request, queryset, parameters):
    """ 
    Genera un Wiki Temmplate a partir de ViewDefinition 

    """

#   QSet User selection registers ( Ids ) 
    if queryset.count() < 1:
        return  {'success':False, 'message' : 'Multiple selection required'}


    try:
        result = doWikiTemplate(request, queryset, parameters)

    except Exception as e:
        traceError()
        result = {'success':False, 'message' : getReadableError(e) }

    return result

