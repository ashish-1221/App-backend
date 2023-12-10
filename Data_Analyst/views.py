from .serializers import VillageBoundaryModelSerializer
from rest_framework import viewsets
from .models import *
from django_filters import rest_framework as filters
from rest_framework.permissions import IsAuthenticated

class VillageBoundaryViewsetFilter(filters.FilterSet):
    class Meta:
        model = VillageBoundaryModel
        fields = ['state_name']

class VillageBoundaryViewset(viewsets.ModelViewSet):
    #authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes=[IsAuthenticated]
    queryset = VillageBoundaryModel.objects.all()
    serializer_class = VillageBoundaryModelSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('state_name',)

# class VillageLocalityViewsetFilter(filters.FilterSet):
#     class Meta:
#         model = VillageLocalityModel
#         fields = ['state_name','']


    