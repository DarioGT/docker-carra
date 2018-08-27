# -*- coding: utf-8 -*-

import json
from django.forms.models import model_to_dict
from protoExt.utils.downloadFile import getCustomPath
from rqGraph.models import NodeStyle, EdgeStyle, Cluster, Canvas, CanvasDetail,\
    ClusterNodes, Edge
 


VersionSoftBPM = "0.0.1-2018-07-31"
nLn = '\l' # New Line 

graphSettings = {}
GVDescription = ""
clusterStucture = {}

# Unique instance collections 
clustersAll = {}
nodesAll = {}
edgesAll = []

# Styles 
nodeStyleCll= {}
edgeStyleCll = {}


def CreateSoftBPM( canvasId ):

    #Cavas::Cluster Setting     
    graphSettings = Canvas.objects.get( id = canvasId )

    #Start the Graph
    GVDescription = "//graphviz file generated with SoftBPM " + VersionSoftBPM + nLn
    GVDescription = GVDescription + "digraph \""  + graphSettings[ 'graphName' ] + "\"{" + nLn


    #Cluster Hierarchy
    for cluster in CanvasDetail.objects.filter( canvas_id = canvasId ): 
        clusterDict = model_to_dict(cluster) 
        clusterDict['clusters_set'] = getClusterHierarchy( clusterDict )
        clusterDict['nodes_set'] = getClusterNodes( clusterDict['id'] )

        clusterStucture[ cluster['code'] ] = clusterDict
        clustersAll[ cluster['code'] ] = clusterDict
    
    #Styles 
    getStyles()
   
    #Cluster loop 
    for cluster in clusterStucture:
        generateGV( cluster )

    #Edges loop 
    for edge in edgesAll:
        generateEdge( edge )

    produceOutput()


def getClusterHierarchy( clusterDict ):
    
    clusterCll = [] 

    #Add Clusters Childs ( others cluster clusters are allowed ) 
    for cluster in Cluster.objects.filter( id = clusterDict['id'] ): 
        clusterChild =  model_to_dict(cluster) 
        clusterCll.append( clusterChild   )
        clusterDict['clusters_set'] = getClusterHierarchy( clusterChild )
        clusterDict['nodes_set'] = getClusterNodes( clusterDict['id'] )

    return clusterCll 


def getClusterNodes( clusterId ):
    
    nodesCll = []

    #Add Clusters Nodes and Edges ( others cluster nodes are allowed ) 
    for node in ClusterNodes.objects.filter( id = clusterId ): 
        nodeDict =  model_to_dict(node) 
        nodesCll.append( nodeDict )
        nodesAll.append( nodeDict )

        
        for edge in Edge.objects.filter( node0_id = nodeDict['id'] ): 
            edgesAll.append( model_to_dict(edge) )
    
    return nodesCll


def getStyles():

    nodeStyleSet = ()
    edgeStyleSet = ()
  
    # Styles Id
    for node in nodesAll:
        nodeStyleSet.add( node['stile_id'] ) 
      
    for edge in nodesAll:
        edgeStyleSet.add( edge['stile_id'] ) 
  
  
    # Styles Get 
    for node in NodeStyle.objects.filter( pk__in=nodeStyleSet):
        nodeStyleCll[ node['code']] = model_to_dict( node ) 

    for edge in EdgeStyle.objects.filter( pk__in=edgeStyleSet) :
        edgeStyleCll[ node['code']]  = model_to_dict( edge ) 
      

def getClusterStyle( cluster ):

    GVDescription = GVDescription + "tooltip= """ + cluster['description'] + "\";" + nLn

    if not graphSettings.Item("clusterLabelAsNode"):
        GVDescription = GVDescription + "label= """ + cluster['name'] + "\";" + nLn
    else:
        GVDescription = GVDescription + "label= \";" + nLn
        GVDescription = GVDescription + "\"" + cluster['name'] + "\"" 
        GVDescription = GVDescription + " [" + styleTypeItem.Value + "label= """ + cluster['Name'] + "\","
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

    style = nodeEdgeSet(  edge['stile_id'] )
    styleGV = style['GVStyle']
    
    if node['label']:
        styleGV += ',' + 'label=\'' + edge['label'] + '\''
    
    return  '[' + styleGV + ']'
 

def generateGV( cluster ):

    GVDescription = GVDescription + "subgraph \"cluster_" + cluster['code'] + "\" {" + nLn
    GVDescription = GVDescription + getClusterStyle( cluster )

    GVDescription = GVDescription + nLn
         
    For Each clusterChild In cluster['cluster_set']
        generateGV( clusterChild )

    For Each node In cluster['nodes_set']
        generateNode( node )
        
      
def generateNode( node ): 

    GVDescription = GVDescription + nLn +  "\'" + node['code'] + '\''
    GVDescription = GVDescription + getNodeStyle( node )

    TEST = clusterNode.Rank
        

def generateEdge( edge ):

    GVDescription = GVDescription + nLn +  '\'' + node['node0'] + '\' -> ' +  '\'' + node['node1'] 
    GVDescription = GVDescription + getNodeStyle( node )
        
        
        
        # Ranks
        GVDescription = GVDescription + nLn
        For Each Rank In cluster[''].Ranks
            RankGroup = "{ rank=" + Rank + " "
            For Each clusterNode In clusterNodes
                If clusterNode.Rank = Rank:
                    RankGroup = RankGroup + "\"" + clusterNode.ID + "\" "
                
                

            
            RankGroup = RankGroup + "}"
            GVDescription = GVDescription + RankGroup + nLn + nLn
        
        
        
        GVDescription = GVDescription + "}" + nLn
    

def produceOutput(): 
    pass 





