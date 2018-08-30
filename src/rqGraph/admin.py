from django.contrib import admin


from .models import Cluster
from .actions import doGraphViz



class AdmNode( admin.ModelAdmin ):
    actions = [ doGraphViz  ]

admin.site.register( Cluster, AdmNode )


