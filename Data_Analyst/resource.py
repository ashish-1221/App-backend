from import_export import resources,fields
from .models import *
import pandas as pd
         
         
class VillageMappingFileResource(resources.ModelResource):
    state = fields.Field(attribute='state',column_name="state")
    ac_no = fields.Field(attribute="ac_no",column_name="ac_no")
    object_id = fields.Field(attribute="object_id",column_name="object_id")
    name = fields.Field(attribute="name",column_name="name")
    locality = fields.Field(attribute="locality",column_name="locality")
    booth = fields.Field(attribute="booth",column_name="booth")
    probable_nearby_vil_voter = fields.Field(attribute="probable_nearby_vil_voter",column_name="probable_nearby_vil_voter")
    mandal = fields.Field(attribute="mandal",column_name="mandal")

    class Meta:
        model=VillageMappingFile
        

    
        
    
    
    
    