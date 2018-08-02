from django.contrib import admin

# Register your models here.


from .models import Source
from .actions import doGraphMerveille

class MySource( admin.ModelAdmin ):
    actions = [ doGraphMerveille  ]

admin.site.register( Source, MySource )



