from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import VillageMappingFileSerializer

def index(request):
    return render(request, 'albums/albums.html')


class VillageMappingFileViewSet(viewsets.ModelViewSet):
    queryset = VillageMappingFile.objects.all().order_by('state')
    serializer_class = VillageMappingFileSerializer