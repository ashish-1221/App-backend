from rest_framework import serializers
from .models import VillageMappingFile,VillageLocalityModel,State

class StateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    class Meta:
        model=State
        fields =('id','state',)
    
class VillageMappingFileSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    class Meta:
        model = VillageMappingFile
        fields = ('state','ac_no','object_id','name','locality','booth','probable_nearby_vil_voter','mandal')
        datatables_always_serialize = ('id',)
    