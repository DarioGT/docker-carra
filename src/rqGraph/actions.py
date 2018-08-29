# -*- coding: utf-8 -*-

import json
from django.forms.models import model_to_dict
from protoExt.utils.downloadFile import getCustomPath
from rqGraph.models import Node, ClusterHierarchy, Edge, NodeStyle, EdgeStyle
from django.db.models.query_utils import Q


# from protoExt.utils.utilsBase import getReadableError, traceError



VersionSoftBPM = "0.0.1-2018-07-31"
nLn = '\l' # New Line 

GVDescription = ""


# Unique instance collections 
nodesAll = {}


# recorrer las conexiones de los nodos q estan en el diagrama 
idNodes = []
edgesAll = []

# Styles 
nodeStyleSet= {}
edgeStyleSet = {}


def doGraphViz(modeladmin, request, queryset, parameters):
    """ 
    """
    # if queryset.count() < 1:
    #     return  {'success':False, 'message' : 'No record selected' }


    CreateSoftBPM( queryset[1].id )




def CreateSoftBPM( canvasId ):

    # recorrer la jerarquia,  armar la estructuraa, incluir los nodos 
    nodeStruct = {}

    #Cavas::node Setting     
    node = Node.objects.get( id = canvasId )
    nodeStruct['canvas'] = node

    #Start the Graph
    GVDescription = "//graphviz file generated with SoftBPM " + VersionSoftBPM + nLn
    GVDescription = "//RootNode : " + node['code']

    GVDescription += "digraph \""  + node[ 'graphName' ] + "\"{" + nLn

    nodeStruct['nodes_set'] = getHierarchy( node.id )
    getEdges()

   
    #Styles 
    getStyles()
   
    #node loop 
    for node in nodeStruct:
        generateGV( node )

    #Edges loop 
    for edge in edgesAll:
        generateEdge( edge )

    produceOutput()


def getHierarchy( nodeId  ):
    
    # recorrer la jerarquia,  armar la estructuraa, incluir los nodos 
    nodeStruct = {}

    #Cavas::node Setting     
    node = Node.objects.get( id = nodeId )
    nodeStruct['code'] = node.element.code
    nodeStruct['node'] = node.element


    #node Hierarchy
    for clusterElto in ClusterHierarchy.objects.filter( container_id = node.element.id ): 

        nodeid = clusterElto.elemento.id
        nodesAll[ clusterElto.element.code ] =  model_to_dict( clusterElto.element )

        if clusterElto.element.isCluster: 
            nodeStruct['nodes_set'] = getHierarchy( nodeid )
        
        else: 
            idNodes.append = nodeid 


    return nodeStruct


def getEdges():
    

    #Add  Edges 
    for edge in Edge.objects.filter(  Q( 'node0_id' in idNodes ) | Q( 'node1_id' in idNodes )) : 
        edgesAll.append( edge ) 
    


def getStyles():

  
    # Styles Id
    for node in nodesAll:
        nodeStyleSet.add( node['stile_id'] ) 
      
    for edge in nodesAll:
        edgeStyleSet.add( edge['stile_id'] ) 
  
  
    # Styles Get 
    for node in NodeStyle.objects.filter( pk__in=nodeStyleSet):
        nodeStyleSet[ node['code']] = model_to_dict( node ) 

    for edge in EdgeStyle.objects.filter( pk__in=edgeStyleSet) :
        edgeStyleSet[ node['code']]  = model_to_dict( edge ) 
      

def genereNodeStyle( node ):

    GVDescription = GVDescription + "tooltip= """ + node['description'] + "\";" + nLn

    if not node.Item("nodeLabelAsNode"):
        GVDescription = GVDescription + "label= """ + node['name'] + "\";" + nLn
    else:
        GVDescription = GVDescription + "label= \";" + nLn
        GVDescription = GVDescription + "\"" + node['name'] + "\"" 
        GVDescription = GVDescription + " [" + node.Value + "label= """ + node['Name'] + "\","
        GVDescription = GVDescription + "style= \", shape=""plaintext""];" + nLn + nLn
    
    GVDescription = GVDescription + "style = invis;" + nLn


def getNodeStyle( node ):

    style = nodeStyleSet(  node['stile_id'] )
    styleGV = style['GVStyle']
    
    nodeLabel = node['code']
    if node['label']:
        nodeLabel = node['label']
    
    styleGV += ',' + 'label=\'' + node['label'] + '\''

    if node['description']:
        styleGV += ',' + 'tooltip=\'' + node['description'] + '\''


    return  '[' + styleGV + ']'


def getEdgeStyle( edge ):

    style = edgeStyleSet(  edge['stile_id'] )
    styleGV = style['GVStyle']
    
    if edge['label']:
        styleGV += ',' + 'label=\'' + edge['label'] + '\''
    
    return  '[' + styleGV + ']'
 

def generateGV( node ):

    GVDescription = GVDescription + "subgraph \"node_" + node['code'] + "\" {" + nLn
    GVDescription = GVDescription + genereNodeStyle( node )

    GVDescription = GVDescription + nLn
         
    for nodeChild in node['node_set']:
        generateGV( nodeChild )

    for node in node['nodes_set']:
        generateNode( node )
        
      
def generateNode( node ): 

    GVDescription = GVDescription + nLn +  "\'" + node['code'] + '\''
    GVDescription = GVDescription + getNodeStyle( node )

#     TEST = nodeNode.Rank
        

def generateEdge( edge ):

    GVDescription = GVDescription + nLn +  '\'' + edge['node0'] + '\' -> ' +  '\'' + edge['node1'] 
    GVDescription = GVDescription + getNodeStyle( edge )
        
        
        
    # Ranks
    GVDescription +=  nLn
#     for  Rank in node[''].Ranks:
#         RankGroup = "{ rank=" + Rank + " "
#         for nodeNode In nodeNodes: 
#             If nodeNode.Rank = Rank:
#                 RankGroup = RankGroup + "\"" + nodeNode.ID + "\" "
#             

        
#         RankGroup = RankGroup + "}"
#         GVDescription = GVDescription + RankGroup + nLn + nLn
    
    
    
    GVDescription = GVDescription + "}" + nLn
    

def produceOutput(): 
    pass 





