# -*- coding: utf-8 -*-

from protoExt.utils.utilsBase import verifyStr  

def doGraphMerveille(modeladmin, request, queryset, parameters):
    """ 
    to generate graphs
    """

    from protoGraph.models import NodeCategory, EdgeCategory, Node, Edge 
    from protoLib.getStuff import getUserProfile 

    userProfile = getUserProfile( request.user )


#   El QSet viene con la lista de Ids  
    if queryset.count() == 0:
        return  {'success':False, 'message' : 'No record selected' }


    bClean = "" 
    if len(parameters) == 1:
        bClean = parameters[0]['value']  
    

    jAux  = {
        'smOwningTeam' : userProfile.userTeam,
        'smOwningUser' : request.user,
        'smCreatedBy' :  request.user
    }


    # Clean 
    if bClean == "1":
        Node.objects.all().delete()  
        Edge.objects.all().delete() 
        NodeCategory.objects.all().delete() 
        EdgeCategory.objects.all().delete() 


    # Catetegories Nodes Principaux 
    catSource = NodeCategory.objects.get_or_create( code = 'Source', defaults = jAux)[0]
    catResponsable = NodeCategory.objects.get_or_create( code = 'Responsable', defaults = jAux)[0]
    catFichier = NodeCategory.objects.get_or_create( code = 'Fichier', defaults = jAux)[0]

    # Catetegories de Nodes de Relation 
    hubSrcResponsable = NodeCategory.objects.get_or_create( code = 'HubResponsable', defaults = jAux)[0]
    hubSrcFichier = NodeCategory.objects.get_or_create( code = 'HubFichier', defaults = jAux)[0]
    hubSrcDependance = NodeCategory.objects.get_or_create( code = 'HubDepend', defaults = jAux)[0]

    # Edge Catetegories
    edgSrcResponsable0 = EdgeCategory.objects.get_or_create( code = 'SrcResponsable0', defaults = jAux)[0]
    edgSrcFichier0 = EdgeCategory.objects.get_or_create( code = 'SrcFichier0', defaults = jAux)[0]
    edgSrcDependance0 = EdgeCategory.objects.get_or_create( code = 'SrcDependance0', defaults = jAux)[0]

    edgSrcResponsable1 = EdgeCategory.objects.get_or_create( code = 'SrcResponsable1', defaults = jAux)[0]
    edgSrcFichier1 = EdgeCategory.objects.get_or_create( code = 'SrcFichier1', defaults = jAux)[0]
    edgSrcDependance1 = EdgeCategory.objects.get_or_create( code = 'SrcDependance1', defaults = jAux)[0]


    def newEdge( hubType, node0, node1  ):

        edgAux = Edge.objects.get_or_create(
            category = hubType, 
            node0 = node0, 
            node1 = node1, 
            code =  hubType.code, 
            defaults = jAux)[0]
            
        return edgAux


    def newNodeSource( source ):
        # newNode Source and hubFichier
        # Return nSource, nHubFichier 

        nSource = Node.objects.get_or_create(
            category = catSource, 
            idSource = source.id, 
            code = source.code, 
            label = verifyStr( source.label, source.code), 
            defaults = jAux)[0]

       
        nHub = Node.objects.get_or_create(
            category = hubSrcFichier, 
            idSource = source.id, 
            code = source.code, 
            label = hubSrcFichier.code, 
            defaults = jAux)[0]

        newEdge( edgSrcFichier0, nSource, nHub  )

        return nSource, nHub




    def newNodeResponsable( responsable, nSource ):


        # XXX --> IsResposable --> Source 
        nResp = Node.objects.get_or_create(
            category = catResponsable, 
            idSource = responsable.id, 
            code = responsable.code, 
            label = verifyStr( responsable.label, responsable.code), 
            defaults = jAux)[0]
        
        nAux = Node.objects.get_or_create(
            category = hubSrcResponsable, 
            idSource = responsable.id, 
            code = responsable.code, 
            label = hubSrcResponsable.code, 
            defaults = jAux)[0]


        newEdge( edgSrcResponsable0, nResp, nAux  )
        newEdge( edgSrcResponsable1, nAux, nSource  )


    def newNodeResponsableSource( source, nSource ):

        # Responsable 
        try:
            responsable = source.responsable
        except Exception as e:
            return 

        newNodeResponsable( responsable, nSource )


    def newNodeFichier( fichier, nHubFichier, edge ):

        nFichier = Node.objects.get_or_create(
            category = catFichier, 
            idSource = fichier.id, 
            code = fichier.code, 
            label = verifyStr( fichier.label, fichier.code ), 
            defaults = jAux)[0]

        newEdge( edge, nFichier, nHubFichier  )

        return nFichier


    # Sources 
    for source in queryset:

        nSource, nHubFichier = newNodeSource(source)
        newNodeResponsableSource( source, nSource )

        # Source  --> contiens --> fichiers 
        for fichier in source.fichier_set.all(): 
            newNodeFichier( fichier, nHubFichier, edgSrcFichier1 )


        # Dependences 
        newHub = True 
        for s0 in source.dependance_set.all(): 
            # Source  --> depend --> fichiers

            if newHub: 
                newHub = False
                nHubDep = Node.objects.get_or_create(
                    category = hubSrcDependance, 
                    idSource = source.id, 
                    code = source.code, 
                    label = hubSrcDependance.code, 
                    defaults = jAux)[0]

                newEdge( edgSrcDependance0, nSource, nHubDep  )


            nFichier = newNodeFichier( s0.fichier, nHubDep, edgSrcDependance1 )
            nSource, nHubFichier = newNodeSource( s0.fichier.source )
            newEdge( edgSrcFichier1, nHubFichier, nFichier  )

            newNodeResponsableSource( s0.fichier.source, nSource )


    return {'success':True , 'message' :  'Ok' }


