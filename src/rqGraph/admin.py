from django.contrib import admin


from .models import Cluster
from .actions import doGraph



class AdmNode( admin.ModelAdmin ):
    actions = [ doGeneraBasicNet  ]

admin.site.register( Node, AdmNode )


