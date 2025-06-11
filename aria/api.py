from rest_framework import viewsets
from .models import Sede, Reunion, Asistencia
from .serializers import SedeSerializer, ReunionSerializer, AsistenciaSerializer

class SedeViewSet(viewsets.ModelViewSet):
    queryset = Sede.objects.all()
    SedeSerializer_class = SedeSerializer

class ReunionViewSet(viewsets.ModelViewSet):
    queryset = Reunion.objects.all()
    ReunionSerializer_class = ReunionSerializer

class AsistenciaViewSet(viewsets.ModelViewSet):
    queryset = Asistencia.objects.all()
    AsistenciaSerializer_class = AsistenciaSerializer