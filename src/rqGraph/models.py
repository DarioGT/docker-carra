# -*- coding: utf-8 -*-

from django.db import models
from protoExt.utils.utilsConvert import slugify2
from protoLib.models.protomodel import ProtoModelBase, ProtoModelExt 


class NodeStyle(ProtoModelExt):
    code  = models.CharField(blank=True, null=True, max_length=200)
    description = models.CharField(blank=True, null=True, max_length=200)

    fontname = models.CharField(blank=True, null=True, max_length=200)	
    fontsize = models.CharField(blank=True, null=True, max_length=200)
    fontcolor = models.CharField(blank=True, null=True, max_length=200)
    fixedsize = models.BooleanField(default=False)

    width = models.IntegerField(blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)	
    shape = models.CharField(blank=True, null=True, max_length=200)
    style = models.CharField(blank=True, null=True, max_length=200)
    fillcolor = models.CharField(blank=True, null=True, max_length=200)	
    gradientangle = models.CharField(blank=True, null=True, max_length=200)
    color = models.CharField(blank=True, null=True, max_length=200)
    imagePath = models.CharField(blank=True, null=True, max_length=800)

    gvParams = models.CharField(blank=True, null=True, max_length=800)

    def __str__(self):
        return slugify2(self.code )

    unicode_sort = ('code',)



class EdgeStyle(ProtoModelExt):
    code  = models.CharField(blank=True, null=True, max_length=200)
    description = models.CharField(blank=True, null=True, max_length=200)

    dir	 = models.CharField(blank=True, null=True, max_length=200)
    color = models.CharField(blank=True, null=True, max_length=200)

    arrowhead = models.CharField(blank=True, null=True, max_length=200)	
    arrowtail = models.CharField(blank=True, null=True, max_length=200)
    arrowsize = models.IntegerField(blank=True, null=True)

    xlabel = models.CharField(blank=True, null=True, max_length=200)
    style = models.CharField(blank=True, null=True, max_length=200)
    lhead = models.CharField(blank=True, null=True, max_length=200)
    ltail = models.CharField(blank=True, null=True, max_length=200)

    constraint = models.BooleanField(default=False)

    fontname = models.CharField(blank=True, null=True, max_length=200)	
    fontsize = models.CharField(blank=True, null=True, max_length=200)
    fontcolor = models.CharField(blank=True, null=True, max_length=200)

    gvParams = models.CharField(blank=True, null=True, max_length=800)

    def __str__(self):
        return slugify2(self.code )

    unicode_sort = ('code',)



class Node(ProtoModelExt):
    """
    Los nodos son jerarquicos, los padres necesariamente son clusters 
    Un canvas puede contener  nodos / clusters, a diferentes niveles. 
    Los graficos se pueden generar a partir de  clusters
    """

    code  = models.CharField(blank=True, null=True, max_length=200)
    sytle = models.ForeignKey( NodeStyle, blank= True, null= True)

    label  = models.CharField(blank=True, null=True, max_length=200)
    description  = models.CharField(blank=True, null=True, max_length=200)

    visible = models.BooleanField(blank=True, default=True)
    url = models.CharField(blank=True, null=True, max_length=800)

#   Cluster ( AutoReference )
    isCluster = models.BooleanField(default=False)
    labelAsNode = models.BooleanField(default=False)
    hideNodes = models.BooleanField(default=False)

#   Optional params 
    gvParams = models.CharField(blank=True, null=True, max_length=800)

#   Trace Origin 
    idContenttype  = models.IntegerField(blank=True, null=True)
    idSource  = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return slugify2(self.code )

    unicode_sort = ('code','style')


class ClusterManager( models.Manager ): 
    def get_queryset(self):
        bCluster = False
        if self.model._meta.model_name == 'cluster': 
            bCluster = True
        return super(ClusterManager, self).get_queryset().filter( isCluster = bCluster )

    
class Cluster(Node):
    objects = ClusterManager()

    class Meta: 
        proxy = True 

    def save(self, *args, **kwargs):
        self.isCluster = True
        super(ProtoModelBase, self).save(*args, **kwargs)


    protoExt = {
        "gridConfig": {
            "listDisplay": ["code", "label", "description"]
        },
        "actions": [
            {"name": "doGraphViz", "selectionMode": "single"},
        ],
    }


class NodeLink(Node):
    objects = ClusterManager()

    class Meta: 
        proxy = True 



class Edge(ProtoModelExt):
    #The edges connect nodes, only edges connecting nodes of the selected clusters are graphed
    code  = models.CharField(blank=True, null=True, max_length=200)
    style = models.ForeignKey( EdgeStyle, blank= True, null= True)

    node0 = models.ForeignKey( Node, blank= True, null= True, related_name='node0_set')
    node1 = models.ForeignKey( Node, blank= True, null= True, related_name='node1_set')

    label  = models.CharField(blank=True, null=True, max_length=200)
    description  = models.CharField(blank=True, null=True, max_length=200)
    url = models.CharField(blank=True, null=True, max_length=800)
    

    def __str__(self):
        return slugify2(self.code )


class ClusterHierarchy(ProtoModelBase):
    # El canvas no es mas q una herarquia de elementos 
    # Los elementos descriptivos estan eb ek nodo container
    container = models.ForeignKey( 'Node', blank= True, null= True, related_name='container_set')
    element = models.ForeignKey( 'Node', blank= True, null= True, related_name='element_set')

    rankType = models.CharField(blank=True, null=True, max_length=20)
    rank = models.CharField(blank=True, null=True, max_length=200)
    sequence = models.IntegerField(blank=True, null=True) 


    def __str__(self):
        return slugify2(self.container + ' > ' + self.element)

    unicode_sort = ('container', 'element')



# ShapeType = ( 'box', 'polygon', 'ellipse', 'oval', 'circle', 'point', 'egg','triangle','plaintext','diamond','trapezium','parallelogram','house','pentagon','hexagon','septagon','octagon',doublecircle','doubleoctagon','tripleoctagon','invtriangle','invtrapezium','invhouse','Mdiamond','Msquare','Mcircle', 'rect','rectangle','square','cylinder','note','tab','folder','box3d','component','promoter','cds','terminator','utr','primersite','restrictionsite','fivepoverhang','threepoverhang','noverhang','assembly','signature','insulator','ribosite','rnastab','proteasesite','proteinstab','rpromoter','rarrow','larrow','lpromote' ) 
# StyleType = ( '', solid','dotted','filled','invisible','diagonals','rounded','dashed','bold','dotted,filled','rounded,filled','solid,filled','dashed,filled','dashed,rounded,filled' )
# ArrowDirection = ('', 'forward','back','both','none' )
# ArrowType = ( '','normal','dot','odot','none','empty','diamond','ediamond','box','open','vee','inv','invdot','invodot','tee', 'crow','obox','halfopen' )
# RankType = ( '','same','min','max','source','sink' )
# GraphType =('','dot','neato','dotty','circo','fdp','nop','nop1','nop2','osage','patchwork','sfdp','twopi' )
# ArrowType = ('','normal','dot','odot','none','empty','diamond','ediamond','box','open','vee','inv','invdot','invodot','tee','invempty','odiamond','crow','obox','halfopen' )
# RankType = ('','same','min','max','source','sink' )
# GraphType =('','dot','neato','dotty','circo','fdp','nop','nop1','nop2','osage','patchwork','sfdp','twopi' )
