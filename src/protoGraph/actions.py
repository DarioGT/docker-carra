# -*- coding: utf-8 -*-

import json
from protoExt.utils.downloadFile import getCustomPath

# from protoExt.utils.utilsBase import getReadableError, traceError

def doGeneraBasicNet(modeladmin, request, queryset, parameters):
    """ 
    to genetate nodes and edges 
		  var nodes = new vis.DataSet([
		    {id: 1, label: 'Node 1'},
		    {id: 2, label: 'Node 2'},
		    {id: 3, label: 'Node 3'}
		  ]);

		  // create an array with edges
		  var edges = new vis.DataSet([
		    {from: 1, to: 2},
		    {from: 1, to: 3},
		  ]);

    """
    # if queryset.count() < 1:
    #     return  {'success':False, 'message' : 'No record selected' }


    from protoGraph.models import Edge, Node
     
    nodes = []
    edges = []

    for edge in Edge.objects.all(): 
        edges.append( { 'from' : edge.node0.id, 'to': edge.node1.id })

    for node in Node.objects.all(): 
        nodes.append( { 
            'id' : node.id, 
            'label': node.label,   
            'title': node.code, 
            'group': node.category.code 
            })


#   jsonfiles 
    fileName = 'graphNodes.js'
    fullPath =  getCustomPath( 'visjs', fileName )

    with open(fullPath, 'w') as file:
        file.write('nodes = ' + json.dumps(nodes)) 

#   jsonfiles 
    fileName = 'graphEdges.js'
    fullPath =  getCustomPath( 'visjs', fileName )

    with open(fullPath, 'w') as file:
        file.write('edges = ' + json.dumps(edges)) 


    return {'success':True , 'message' :  'Ok' }


