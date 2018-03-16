from django.contrib import admin

# Register your models here.


from .models import Edge
from .actions import doGeneraBasicNet

class AdmEdge( admin.ModelAdmin ):
    actions = [ doGeneraBasicNet  ]

admin.site.register( Edge, AdmEdge )



