# -*- coding: utf-8 -*-

from protoExt.utils.utilsBase import verifyStr  

def doGraphMerveille(modeladmin, request, queryset, parameters):
    """ 
    to generate graphs
    """

    from rqEirq.models import Source 
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


    def creaResponsable( responsable, nSource ):

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

        edgAux = Edge.objects.get_or_create(
            category = edgSrcResponsable0, 
            node0 = nResp, 
            node1 = nAux, 
            code = edgSrcResponsable0.code, 
            defaults = jAux)[0]

        edgAux = Edge.objects.get_or_create(
            category = edgSrcResponsable1, 
            node0 = nAux, 
            node1 = nSource, 
            code = edgSrcResponsable1.code, 
            defaults = jAux)[0]


    # Sources 
#   Recorre los registros selccionados   
    # Source.objects.all(): 
    for source in queryset:

        # ????  -> IsResposable --> Source 
        nSource = Node.objects.get_or_create(
            category = catSource, 
            idSource = source.id, 
            code = source.code, 
            label = verifyStr( source.label, source.code), 
            defaults = jAux)[0]

        # Responsable 
        try:
            responsable = source.responsable
            creaResponsable( responsable, nSource )
        except Exception as e:
            pass 


        # Source  --> contiens --> ???  ( fichiers )
        nAux = Node.objects.get_or_create(
            category = hubSrcFichier, 
            idSource = source.id, 
            code = source.code, 
            label = hubSrcFichier.code, 
            defaults = jAux)[0]


        edgAux = Edge.objects.get_or_create(
            category = edgSrcFichier0, 
            node0 = nSource, 
            node1 = nAux, 
            code =  edgSrcFichier0.code, 
            defaults = jAux)[0]


        for fichier in source.fichier_set.all(): 
            # Source  --> contiens --> ???  ( fichiers )

            nFichier = Node.objects.get_or_create(
                category = catFichier, 
                idSource = fichier.id, 
                code = fichier.code, 
                label = verifyStr( fichier.label, fichier.code ), 
                defaults = jAux)[0]

            edgAux = Edge.objects.get_or_create(
                category = edgSrcFichier1, 
                node0 = nAux, 
                node1 = nFichier, 
                code =  edgSrcFichier1.code, 
                defaults = jAux)[0]


        newHub = True 
        for s0 in source.dependance_set.all(): 
            # Source  --> depend --> ???  ( fichiers )

            if newHub: 
                newHub = False
                nAux = Node.objects.get_or_create(
                    category = hubSrcDependance, 
                    idSource = source.id, 
                    code = source.code, 
                    label = hubSrcDependance.code, 
                    defaults = jAux)[0]

                edgAux = Edge.objects.get_or_create(
                    category = edgSrcDependance0, 
                    node0 = nSource, 
                    node1 = nAux, 
                    code =  edgSrcDependance0.code, 
                    defaults = jAux)[0]

            nFichier = Node.objects.get_or_create(
                category = catFichier, 
                idSource = s0.fichier.id, 
                code = s0.fichier.code, 
                label = verifyStr( s0.fichier.label, s0.fichier.code ), 
                defaults = jAux)[0]

            edgAux = Edge.objects.get_or_create(
                category = edgSrcDependance1, 
                node0 = nAux, 
                node1 = nFichier, 
                code =  edgSrcDependance1.code, 
                defaults = jAux)[0]



    return {'success':True , 'message' :  'Ok' }