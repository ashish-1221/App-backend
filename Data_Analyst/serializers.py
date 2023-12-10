from rest_framework import serializers
from .models import VillageMappingFile,VillageBoundaryModel
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from django_filters import rest_framework as filters


# class StateSerializer(serializers.ModelSerializer):
#     id = serializers.IntegerField()
#     class Meta:
#         model=State
#         fields =('id','state_name',)
    
class VillageMappingFileSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    class Meta:
        model = VillageMappingFile
        fields = ('state_name','ac_no','object_id','name','locality','booth','probable_nearby_vil_voter','mandal')
        datatables_always_serialize = ('id',)


class VillageBoundaryModelSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = VillageBoundaryModel
        geo_field="geometry"
        id_field= "state_name"
        fields = ('state_name','object_id','v_id','name','distric','subdistric','censusname','lgd_villag','level_2011','tru_2011',"mapping_file")
