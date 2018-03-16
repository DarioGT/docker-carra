# -*- coding: utf-8 -*-

import json
from protoExt.utils.downloadFile import getFullPath

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
        nodes.append( { 'id' : node.id, 'label': node.label })


#   jsonfiles 
    fileName = 'graphNodes.json'
    fullPath = getFullPath(request, fileName)

    with open(fullPath, 'w') as file:
        file.write(json.dumps(nodes)) # use `json.loads` to do the reverse

#   jsonfiles 
    fileName = 'graphEdges.json'
    fullPath = getFullPath(request, fileName)

    with open(fullPath, 'w') as file:
        file.write(json.dumps(edges)) # use `json.loads` to do the reverse


    return {'success':True , 'message' :  'Ok' }


