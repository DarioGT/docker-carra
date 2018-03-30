from django.contrib import admin

# Register your models here.


from .models import Edge, Node 
from .actions import doGeneraBasicNet

class AdmEdge( admin.ModelAdmin ):
    actions = [ doGeneraBasicNet  ]

admin.site.register( Edge, AdmEdge )



class AdmNode( admin.ModelAdmin ):
    actions = [ doGeneraBasicNet  ]

admin.site.register( Node, AdmNode )


