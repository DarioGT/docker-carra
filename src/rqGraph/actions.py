# -*- coding: utf-8 -*-

import json
from protoExt.utils.downloadFile import getCustomPath
from rqGraph.models import Node, ClusterHierarchy, Edge, NodeStyle, EdgeStyle
from django.db.models.query_utils import Q
from datetime import datetime


# from protoExt.utils.utilsBase import getReadableError, traceError


VersionSoftBPM = '0.0.1'

# Unique instance collections 
nodesAll = {}

# recorrer las conexiones de los nodos q eststylean en el diagrama 
idNodes = []
edgesAll = []

# Styles 
nodeStyleSet= {}
edgeStyleSet = {}
datetime

def doGraphViz(modeladmin, request, queryset, parameters):
    ''' 
    '''
    if queryset.count() < 1:
        return  {'success':False, 'message' : 'No record selected' }


    CreateSoftBPM( queryset[0].id )
    
    pass


def CreateSoftBPM( canvasId ):

    # recorrer la jerarquia,  armar la estructuraa, incluir los nodos 
    nodeStruct = {}

    #Cavas::node Setting     
    node = Node.objects.get( id = canvasId )
    nodeStruct['canvas'] = node

    #Start the Graph
    GVsrc = '//SoftMachine Graph v(0) {1}\n'.format( VersionSoftBPM, datetime.now() )
    GVsrc += 'digraph "{0}"'.format( node.code ) +  "{\n"
    GVsrc += getNodeStyle(node) + '\n' 

    #Add  Hierarchy
    nodeStruct['nodes_set'], sAux  = getHierarchy( node.id )
    GVsrc += sAux


    #Add  Edges
    GVsrc +=  getEdges()
    GVsrc += "}" 

    pass



def getEdges():

    sAux = ''
    #Add  Edges 
    for edge in Edge.objects.filter(  Q( node0__pk__in= idNodes ) | Q( node1__pk__in= idNodes )) : 
        sAux  += '"{0}" -> "{1}" [label="{2}"]\n'.format( edge.node0.code,  edge.node1.code, edge.label or '' )
        edgesAll.append( edge ) 

    return sAux 


def getHierarchy( nodeId  ):
    
    # recorrer la jerarquia,  armar la estructuraa, incluir los nodos 
    nodeStruct = {}
    sAux = ''
    

    #Cavas::node Setting     
    nodeRoot = Node.objects.get( id = nodeId )
    nodeStruct['code'] = nodeRoot.code
    nodeStruct['node'] = nodeRoot
    nodeStruct['elements'] = []
    nodeStruct['nodes_set'] = {} 
    
    #node Hierarchy
    for clusterElto in ClusterHierarchy.objects.filter( container_id = nodeRoot.id ): 

        nodeCh = clusterElto.element 
        nodeid = clusterElto.element.id
        nodesAll[ clusterElto.element.code ] = nodeCh

        if nodeCh.isCluster: 
            sAux += 'subgraph "node_{0}"'.format( nodeCh.code ) + '{\n'
            sAux += getNodeStyle(nodeCh) + '\n' 

            nodeStruct['nodes_set'], s2  = getHierarchy( nodeid )
            sAux += s2

        else: 
            nodeStruct['elements'].append( nodeCh ) 
            idNodes.append( nodeid )  

            sAux +=  '{0} [{1}]\n'.format( nodeCh.code, getNodeStyle(nodeCh) ) 
    
        if nodeCh.isCluster: 
            sAux += '}\n' 

    return nodeStruct, sAux 



def getNodeStyle( node ):

    sAux = 'label="{0}"'.format( node.label or node.code )  

    if node.description:
        sAux += ',tooltip="{0}"'.format( node.description  ) 

    sAux = addGvParams( sAux, node.gvParams or '')
    if node.style:  
        sAux = addGvParams( sAux, node.style.gvParams or '' )  

    return  sAux


def addGvParams( sAux, gvParams ):
    # Params hierarchy

    if len( gvParams.strip() ) ==  0:
        return sAux
     
    cParams = sAux.strip().split( ',' )
    cNewParams = gvParams.strip().split( ',' )

    cUnique = []
    for pAux in cParams: 
        cUnique.append( pAux.split('=')[0].strip())

        
    for pAux in cNewParams: 
        pNew = pAux.split('=')[0].strip()
        if pNew in cUnique: continue 
        cUnique.append( pNew )
        sAux += ',' + pAux

    return sAux 



def labelAsNode( node ):

    sAux = ''
    # if not node.Item('nodeLabelAsNode')
    #     sAux += 'label= ''' + node['name'] + '\';' + nL
    # else
    #     sAux += 'label= \';' + nL
    #     sAux += '\'' + node['name'] + '\''
    #     sAux += ' [' + node.Value + 'label= ''' + node['Name'] + '\',
    #     sAux += 'style= \', shape=''plaintext''];' + nLn + nL
   
    # sAux += 'style = invis;' + nL

    # return sAux
    pass


def defineRank():
        
    # for  Rank in node[''].Ranks:
    #     RankGroup = "{ rank=' + Rank + ' '
    #     for nodeNode In nodeNodes: 
    #         If nodeNode.Rank = Rank:
    #             RankGroup = RankGroup + '\'' + nodeNode.ID + '\' '
        
    #     RankGroup = RankGroup + '}"
    #     GVsrc += RankGroup + nLn + nLn
    
    # GVsrc += '}" + nLn
    
    pass 
